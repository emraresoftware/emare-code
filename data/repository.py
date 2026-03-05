from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from sqlalchemy import func

from data.database import Log, Project, get_session, init_db

init_db()


def _to_datetime(value: Any) -> Optional[datetime]:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, str) and value:
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            return None
    return None


def _project_to_dict(project: Project) -> dict:
    return {
        "name": project.name,
        "language": project.language,
        "description": project.description,
        "platform": project.platform,
        "version": project.version,
        "created_at": project.created_at.isoformat() if project.created_at else None,
        "updated_at": project.updated_at.isoformat() if project.updated_at else None,
    }


def upsert_project(
    name: str,
    language: str,
    description: Optional[str] = None,
    platform: Optional[str] = None,
    version: Optional[str] = None,
) -> dict:
    now = datetime.utcnow()

    with get_session() as session:
        project = session.query(Project).filter_by(name=name).one_or_none()
        if project:
            project.language = language
            if description is not None:
                project.description = description
            if platform is not None:
                project.platform = platform
            if version is not None:
                project.version = version
            project.updated_at = now
        else:
            project = Project(
                name=name,
                language=language,
                description=description,
                platform=platform,
                version=version,
                created_at=now,
                updated_at=now,
            )
            session.add(project)
        session.flush()
        return _project_to_dict(project)


def list_projects() -> list[dict]:
    with get_session() as session:
        projects = session.query(Project).order_by(Project.name.asc()).all()
        return [_project_to_dict(p) for p in projects]


def get_project(name: str) -> Optional[dict]:
    with get_session() as session:
        project = session.query(Project).filter_by(name=name).one_or_none()
        return _project_to_dict(project) if project else None


def remove_project(name: str) -> bool:
    with get_session() as session:
        project = session.query(Project).filter_by(name=name).one_or_none()
        if not project:
            return False
        session.delete(project)
        session.flush()
        return True


def record_log(level: str, message: str, timestamp: Optional[Any] = None) -> None:
    ts = _to_datetime(timestamp) or datetime.utcnow()
    with get_session() as session:
        session.add(Log(timestamp=ts, level=level, message=message))
        session.flush()


def get_last_activity() -> Optional[str]:
    with get_session() as session:
        proj_ts = session.query(func.max(Project.updated_at)).scalar()
        log_ts = session.query(func.max(Log.timestamp)).scalar()

    candidates = [ts for ts in (proj_ts, log_ts) if ts]
    if not candidates:
        return None
    return max(candidates).isoformat()

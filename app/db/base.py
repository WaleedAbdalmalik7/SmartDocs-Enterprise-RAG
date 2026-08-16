import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import enum
class Base(DeclarativeBase):
    pass
class UserRole(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    EMPLOYEE = "employee"
    VIEWER = "viewer"

class DocStatus(str, enum.Enum):
    UPLOADING = "uploading"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
class Organization(Base):
    __tablename__ = "organizations"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    slug: Mapped[str] = mapped_column(sa.String(100), unique=True, index=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    org_id: Mapped[int] = mapped_column(sa.ForeignKey("organizations.id"), nullable=False, index=True)
    email: Mapped[str] = mapped_column(sa.String(255), unique=True, index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    hashed_password: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(default=UserRole.EMPLOYEE)
    is_active: Mapped[bool] = mapped_column(default=True)
class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    org_id: Mapped[int] = mapped_column(sa.ForeignKey("organizations.id"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    category: Mapped[str] = mapped_column(sa.String(50), nullable=True)
    current_version_id: Mapped[int] = mapped_column(sa.ForeignKey("document_versions.id"), nullable=True)


class DocumentVersion(Base):
    __tablename__ = "document_versions"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(sa.ForeignKey("documents.id"), nullable=False, index=True)
    version_number: Mapped[str] = mapped_column(sa.String(20), nullable=False)
    file_path: Mapped[str] = mapped_column(sa.String(500), nullable=False)
    status: Mapped[DocStatus] = mapped_column(default=DocStatus.UPLOADING)
    uploaded_by: Mapped[int] = mapped_column(sa.ForeignKey("users.id"), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True) # للإصدار الحالي
class Conversation(Base):
    __tablename__ = "conversations"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    org_id: Mapped[int] = mapped_column(sa.ForeignKey("organizations.id"), nullable=False, index=True)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(sa.String(255), default="محادثة جديدة")

class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    conversation_id: Mapped[int] = mapped_column(sa.ForeignKey("conversations.id"), nullable=False, index=True)
    role: Mapped[str] = mapped_column(sa.String(20), nullable=False) # user, assistant
    content: Mapped[str] = mapped_column(sa.Text, nullable=False)
    sources: Mapped[str] = mapped_column(sa.Text, nullable=True) # JSON String
class AuditLog(Base):
    __tablename__ = "audit_logs"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    org_id: Mapped[int] = mapped_column(sa.ForeignKey("organizations.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"), nullable=True)
    action: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    resource_type: Mapped[str] = mapped_column(sa.String(50), nullable=True)
    resource_id: Mapped[int] = mapped_column(nullable=True)
    details: Mapped[str] = mapped_column(sa.Text, nullable=True)
    timestamp: Mapped[sa.DateTime] = mapped_column(server_default=sa.func.now())
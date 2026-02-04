"""add description to tasks

Revision ID: 20260204_add_description
Revises: 
Create Date: 2026-02-04 21:40:00
"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260204_add_description"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("tasks", sa.Column("description", sa.String(length=1000), nullable=True))


def downgrade() -> None:
    op.drop_column("tasks", "description")

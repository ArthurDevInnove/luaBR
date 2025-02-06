"""Updating PostsModel

Revision ID: eaac135e98a3
Revises: 
Create Date: 2025-02-04 11:41:19.806004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaac135e98a3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'posts_model',
        'post_hour',
        type_=sa.DateTime()
    )

    op.alter_column(
        'posts_model',
        'title',
        type_=sa.String(90)
    )

    op.add_column(
        'posts_model',
        sa.Column('author_name', sa.String(20), nullable=False)
    )


def downgrade() -> None:
    pass

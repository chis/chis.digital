"""change field

Revision ID: 8b472a65bdbb
Revises: ec28ba8f63b1
Create Date: 2021-08-30 22:45:08.405741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b472a65bdbb'
down_revision = 'ec28ba8f63b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_title', table_name='post')
    op.create_index(op.f('ix_post_title'), 'post', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_title'), table_name='post')
    op.create_index('ix_post_title', 'post', ['title'], unique=False)
    # ### end Alembic commands ###

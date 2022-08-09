"""Init database after add username

Revision ID: 169d4ab1983d
Revises: af3c75f9dca3
Create Date: 2022-08-09 18:24:39.398732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '169d4ab1983d'
down_revision = 'af3c75f9dca3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('has_sale', sa.Boolean(), server_default=sa.text('true'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'has_sale')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
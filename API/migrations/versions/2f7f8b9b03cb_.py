"""empty message

Revision ID: 2f7f8b9b03cb
Revises: 94f432dcd6eb
Create Date: 2019-06-11 23:41:00.311907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f7f8b9b03cb'
down_revision = '94f432dcd6eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('agreementId', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('listOfModules', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'listOfModules')
    op.drop_column('user', 'agreementId')
    # ### end Alembic commands ###

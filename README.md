ECHO is on.

## Setup dor DataBase
First, install and initialize the alembic in your virtual environment:

```
$ cd ../Dual_edu
$ pip install alembic
$ alembic init alembic
```
# Change the sqlalchemy.url in your alembic.ini file:

```
sqlalchemy.url = mysql+mysqldb://root:root@localhost:3306/database_name
```

# Create your model or modify current model.py.
If you created a new model file give your model path to env.py. 

```
from model import Base
target_metadata = Base.metadata
```
# Create migration with command:

```
alembic revision — autogenerate -m “Your commit”
```

# Run the database migration:

```
alembic upgrade head
```
Once you run the above command your tables will be generated in your database.
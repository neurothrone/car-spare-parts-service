from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.employee_repository import EmployeeRepository
else:
    from app.data._mysql.repositories.employee_repository import EmployeeRepository

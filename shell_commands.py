from pickle import FALSE, TRUE
from employee.models import AbstractPerson, Employee, Passport, Workproject, Membership, Client, VIPClient
from datetime import date

aika = Employee.objects.create(name="Aikanysh", birth_date = date(1988, 8, 25), position="administrator", salary=1000, work_experience=6)
tahir = Employee.objects.create(name="Tahir", birth_date = date(2000, 4, 20), position="video editor", salary=500, work_experience=2)
dolat = Employee.objects.create(name="Dolatbek", birth_date = date(1999, 5, 22), position="assistant", salary=500, work_experience=2)
salavat = Employee.objects.create(name="Salavat", birth_date = date(2001, 6, 15), position="developer", salary=800, work_experience=3)

p1 = Passport(employee=aika, inn=12367486, id_card = "P1264748383")
p2 = Passport(employee=tahir, inn = 26365733, id_card = "P2736488379")
p3 = Passport(employee=dolat, inn = 28847483, id_card = "P2949584848")
p4 = Passport(employee=salavat, inn = 28483938, id_card = "P2849504847")

p4 = Passport.objects.get(id=4)
p4.delete()

e = Employee.objects.get(id=5)
e.delete()

codify = Workproject.objects.create(project_name = "Codify")
codify.members.set([aika, tahir, dolat, salavat], through_defaults={'date_joined':date(2022, 4, 5)})
codify.members.remove(salavat)
codify.members.create(name="Kamila", birth_date = date(1995, 7, 25), position="manager", salary=1500, work_experience=4)

daniyar = Client(name="Daniyar", birth_date=(1992, 5, 9), address="Bishkek", phone_number="996770558789")
azaliya = Client(name="Azaliya", birth_date=(1995, 10, 19), address="Kant", phone_number="996770567899")
aijan = Client(name="Aijan", birth_date=(1981, 11, 20), address="Osh", phone_number="996770567710")

nurbek = VIPClient(name="Nurbek", birth_date=(1980, 1, 25), address="Bishkek", phone_number="996550587711", vip_status_start = date(2022, 3, 8), donation_amount = 5000)

client1 = Client.objects.get(name="Aijan")
client1.delete()


all_employees = Employee.objects.all()
print(all_employees)
employees_with_passports = all_employees.filter(Passport__inn__isnull = False, Passport__card_id__isnull = False)
print(employees_with_passports)
all_work_projects = Workproject.objects.all()
print(all_work_projects)
target_employee = Workproject.objects.get(Employee.name == "Aikanysh")
print(target_employee)
all_clients = Client.objects.all()
print(all_clients)
vip_client = VIPClient.objects.all()
print(vip_client)



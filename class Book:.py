class Book:
    def __init__(self,title,author,year,isbn):
        self.__title = title
        self.__author = author
        self.__year=year
        self.__isbn = isbn
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,new_year):
        if new_year < self.__year:
            raise ValueError("New publishing year must be more recent than previous publication")
        else:
            print("Publication date succesfully changed")
            self.__year = new_year 


book1 = Book("The Chrysailds","John",1955,"97801411")
book2 = Book("The Cysailds","Jon",1823,"978014121")
book3 = Book("Therysailds","Joh",1826,"978014114")
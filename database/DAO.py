from database.DB_connect import DBConnect
from model.arco import Arco
from model.customer import Customer


class DAO():
    @staticmethod
    def getAllAlbums():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select * from album
                """

        cursor.execute(query)

        for row in cursor:
            results.append(**row)

        cursor.close()
        conn.close()
        return results


    #DD country
    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select
                    distinct
                    c.Country
                    from customer c
                    order
                    by
                    c.Country """

        cursor.execute(query)

        for row in cursor:
            results.append(row["Country"])

        cursor.close()
        conn.close()
        return results #lista di str country

    #clienti nodi con almeno 1 fattura e memo fatturato totale
    @staticmethod
    def getNodesClienti(paese):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.*, sum(i.Total) as fatturato
                    from customer c, invoice i 
                    where c.CustomerId = i.CustomerId 
                    and c.Country = %s
                    group by c.CustomerId"""

        cursor.execute(query, (paese,)) #con la virgola?

        for row in cursor:
            cliente = Customer(row["CustomerId"], row["FirstName"],row["LastName"],row["Company"],row["Address"],row["City"],row["State"],row["Country"],row["PostalCode"],row["Phone"],row["Fax"],row["Email"],row["SupportRepId"],float(row["fatturato"]))
            results.append(cliente)
        cursor.close()
        conn.close()
        return results #lista di oggetti customer

    #coppie clienti che hanno acquistato dallo stesso artista
    @staticmethod
    def getArchi(paese, idMapClienti):
        conn = DBConnect.get_connection()

        results = [] #lista di oggetti archi

        cursor = conn.cursor(dictionary=True)
        query = """select t1.customerid as c1, t2.customerid as c2 
                    from (select c.CustomerId, ar.ArtistId 
                    from customer c, invoice i, invoiceline il , track t , album al , artist ar 
                    where c.CustomerId =i.CustomerId and i.InvoiceId = il.InvoiceId and il.TrackId = t.TrackId and t.AlbumId = al.AlbumId and al.ArtistId = ar.ArtistId 
                    and c.Country = %s
                    group by c.CustomerId ) t1,
                    (select c.CustomerId, ar.ArtistId 
                    from customer c, invoice i, invoiceline il , track t , album al , artist ar 
                    where c.CustomerId =i.CustomerId and i.InvoiceId = il.InvoiceId and il.TrackId = t.TrackId and t.AlbumId = al.AlbumId and al.ArtistId = ar.ArtistId 
                    and c.Country = %s
                    group by c.CustomerId ) t2
                    where t1.customerid <> t2.customerid 
                    and t1.artistid = t2.artistid 
                    group by t1.customerid, t2.customerid """

        cursor.execute(query, (paese, paese,))  # con la virgola?

        for row in cursor:
            c1 = idMapClienti[row["c1"]]
            c2 = idMapClienti[row["c2"]]
            peso = c1.totaleFatturato + c2.totaleFatturato
            if c1.totaleFatturato > c2.totaleFatturato:
               results.append(Arco(c1,c2,peso))
            elif c2.totaleFatturato>c1.totaleFatturato:
                results.append(Arco(c2,c1,peso))
            else:
                results.append(Arco(c1,c2,peso))
                results.append(Arco(c2,c1,peso))

        cursor.close()
        conn.close()
        return results  # lista di oggetti arco


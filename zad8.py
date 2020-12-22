
import riak


client = riak.RiakClient(host='172.17.0.2')

bucket = client.bucket('s15252')

json = {'name': 'Interstellar', 'director': 'Nolan' , 'lenght':186 , 'rating': 9.2}

movie = bucket.new('Interstellar', data=json)
movie.store()

print(str(bucket.get('Interstellar').data))

update = bucket.get('Interstellar')
update.data['rating'] = 10.0
update.store()


print(str(bucket.get('Interstellar').data))

bucket.get('Interstellar').delete()

print(str(bucket.get('Interstellar').data))
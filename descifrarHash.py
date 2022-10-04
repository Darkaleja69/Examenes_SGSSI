import hashlib
def getmd5file(archivo):
    try:
        hashmd5 = hashlib.md5()
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashmd5.update(bloque)
        return hashmd5.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""
i=1
x = False
while (i<=46 and x==False):		
	with open('/home/darkaleja/Descargas/imagenesPrac/imagen'+str(i)+'.jpg', 'rb') as f: 
	    md5 = hashlib.md5(f.read())
	    hash1=md5.hexdigest()
	    if (hash1 == "e5ed313192776744b9b93b1320b5e268"):
	    	x=True
	    	print ("La imagen con el mensaje secreto es :"+str(i))
	    print(hash1)
	    i=i+1

todo = [
    {"id": "oke","todo": "belajar", "jam": 3},
    {"id": "gas","todo": "masak", "jam": 4}, 
    {"id": "siap","todo": "nyuci", "jam": 5}]
          
while True:
    print("\n===== To-Do List =====")
    print("1. input ke txt")
    print("2. REMOVE ALL")
    print("3. liat todo")
    choice = input("Input choice: ")
        
        
    if choice == '1':
        with open('TasksTodo.txt', 'w') as file:
            for task in todo:
                for key, value in task.items():
                    file.write(f"{key}: {value}\n") 
                file.write("\n") 
        
        todos = [] 
        with open('TasksTodo.txt', 'r') as file:
            entry = {}
            for line in file:
                line = line.strip()  
                if line:  
                    key, value = line.split(': ', 1)
                    entry[key] = value 
                else:  
                    if entry:  
                        todos.append(entry)
                        entry = {}  
            if entry:
                todos.append(entry)
  
#ini untuk Remove all
    elif choice == '2':
        with open('TasksTodo.txt', 'w') as file:
            pass
#sampai sini         
    elif choice == '3':
        for todo in todos:
            print(todo.get('todo'))



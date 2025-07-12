import threading
import time

class Clinic:
    def __init__(self):
        self.visitors_count = threading.Semaphore(value = 5)

    def meet_visitor(self, visitor):

        print(f'Пациент {visitor} заходит в клинику')
        self.visitors_count.acquire()
        
        print(f'Пациент {visitor} ждет своей очереди')
        time.sleep(1)
        
        print(f'Пациент {visitor} зашел в кабинет врача')
        time.sleep(2)
        
        print(f'Пациент {visitor} покинул кабинет врача')
        self.visitors_count.release()

        print(f'Пациент {visitor} покинул клинику')
        self.visitors_count.release()

        

    def visitors(self, count):
                
        for visitors in range(1, count):
            visitor_thread = threading.Thread(target=self.meet_visitor, args=(visitors,))
            
            visitor_thread.start()

if __name__ == '__main__':
    Visitors = Clinic()

    count = 5
    Visitors.visitors(count) 
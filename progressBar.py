import time
from prettytable import PrettyTable

class progressBar():
    fmt="\r{} = {:.1f}% [{}] {}/{} {:.1f}s FPS={:.1f}"
    def __init__(self,name):
        self.name=name
        self.start_time=time.time()
        print('The {} starts at {} .'.format(self.name,time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.start_time))))
        
    def update(self,complete,total,bar_length = 20):
        self.total=total
        self.progress=complete/total if ((complete/total)>0)&((complete/total)<1) else 0 if (complete/total)<0 else 1 
        self.update_time=time.time()
        self.spend_time=self.update_time - self.start_time
        block = int(round(bar_length * self.progress))
        self.fps=float(complete/self.spend_time)
        text=self.fmt.format(self.name,self.progress*100,"#"*block+"-"*(bar_length-block),complete,total,self.spend_time,self.fps)
        print(text,end='')
    
    def end(self):
        self.end_time=time.time()
        print('\nThe {} ends at {} .'.format(self.name,time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.end_time))))
        my_table = PrettyTable()
        my_table.field_names = [ "Total", "Progress","Time(s)", "FPS"]
        my_table.add_row([ self.total,self.progress,round(self.spend_time,1),round(self.fps,1)])
        print(my_table)

def progressBar_decorator(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            pb = progressBar(name)
            progress_generator = func(*args, **kwargs)
            try:
                while True:
                    complete,total = next(progress_generator)
                    pb.update(complete,total)
            except StopIteration as result:
                pb.end()
                return result.value
        return wrapper
    return decorator

if __name__ == '__main__':

    @progressBar_decorator('dummyLoop')
    def dummyLoop():
        '''
        An example:
        must use yield of each steps in the function.
        '''
        nb_iter = 13
        for i in range(nb_iter):
            time.sleep(0.1)
            yield (i + 1),nb_iter
        return f"completed={i+1}/{nb_iter}"

    res = dummyLoop()
    print("result:", res)
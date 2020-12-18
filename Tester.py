# thread_test.py
import multiprocessing as mp
import threading
import ml

def list_append(id, listdata):
    """
    Creates an empty list and then appends a 
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    for i in listdata:
            ml._PredictML(i)

if __name__ == "__main__":
    size = 10000000   # Number of random numbers to add
    threads = 5   # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list 
    jobs = []
    for i in range(0, threads):
        out_list = ["""Science involves extensive study of the behaviour of natural and physical world. The study is conducted by way of research, observation and experimentation. There are several branches of science. These include the natural sciences, social sciences and formal sciences. These broad categories have further been divided into sub categories and sub-sub categories. Physics, chemistry, biology earth science and astronomy form a part of the natural sciences, history, geography, economics, political science, sociology, psychology, social studies and anthropology are a part of the social sciences and formal sciences include mathematics, logic, statistics, decision theory, system theory and computer science.""","""Finally, the jobs are sequentially started and then sequentially "joined". The join() method blocks the calling thread (i.e. the main Python interpreter thread) until the thread has terminated. This ensures that all of the threads are complete before printing the completion message to the console:"""]
        thread = mp.Process(target=list_append( i, out_list))
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

    print("List processing complete.")

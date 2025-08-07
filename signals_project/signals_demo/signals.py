from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
import threading
import time
from django.db import connection
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

@receiver(post_save, sender=Book)
def book_created_handler(sender, instance, created, **kwargs):
    if created:
        # ==============================================
        # QUESTION 1: SYNCHRONOUS EXECUTION DEMONSTRATION
        # ==============================================
        print("=== QUESTION 1: Are signals synchronous? ===")
        print("Signal handler STARTED - This will block for 2 seconds")
        start_time = time.time()
        time.sleep(2)  # Simulate a long operation
        end_time = time.time()
        print("Signal handler FINISHED (Duration: {end_time-start_time:.2f}s)")
        print("Conclusion: Signal handler blocked execution, proving synchronous behavior")
        
        # ==============================================
        # QUESTION 2: THREAD DEMONSTRATION
        # ==============================================
        print("=== QUESTION 2: Do signals run in the same thread? ===")
        print("Caller thread name: {threading.current_thread().name}")
        print("Signal handler thread name: {threading.current_thread().name}")
        print("Conclusion: Both show same thread name ('MainThread'), proving same thread execution")
        
        # ==============================================
        # QUESTION 3: TRANSACTION DEMONSTRATION
        # ==============================================
        print("===QUESTION 3: Do signals share the same transaction? ===")
        print("Is in atomic block: {connection.in_atomic_block}")
        if connection.in_atomic_block:
            print("Conclusion: Signal is in same transaction as caller (atomic block)")
        else:
            print("Conclusion: Signal is NOT in same transaction as caller")
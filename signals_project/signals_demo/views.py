from django.http import HttpResponse
from .models import Book
from django.db import transaction
import threading
import time
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def test_signals(request):
    response_lines = []
    
    # ==============================================
    # TEST 1: DEFAULT TRANSACTION BEHAVIOR
    # ==============================================
    print("TEST 1: Creating Book in DEFAULT transaction context")
    Book.objects.create(title="Default Transaction Book", author="Test Author")
    
    # Brief pause between tests for clarity
    time.sleep(1)
    
    # ==============================================
    # TEST 2: EXPLICIT TRANSACTION BEHAVIOR
    # ==============================================
    print("TEST 2: Creating Book in EXPLICIT transaction.atomic() block")
    with transaction.atomic():
        print(" Main thread name inside atomic block: {threading.current_thread().name}")
        Book.objects.create(title="Explicit Transaction Book", author="Test Author")
    
    return HttpResponse("Signal tests completed. Check your console output for detailed analysis.")
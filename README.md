# Django Signals and Python Custom Classes Demonstration

This project demonstrates two key aspects:

1. **Django Signals behavior** (synchronous execution, thread behavior, and transaction handling)  
2. **Python custom iterable class** (Rectangle class with iteration support)

---

## 📁 Project Structure

```
project_root/
├── signals_project/       # Django project demonstrating signals
│   ├── signals_demo/      # Main app with signal demonstrations
│   └── ...                # Other Django project files
└── Custom-Classes/        # Python custom Rectangle class implementation
    └── Rectangle.py       # Rectangle class implementation
```

---

## 🧩 Part 1: Django Signals Demonstration

### ✅ Question 1: Synchronous Execution

**Are Django signals executed synchronously by default?**  
✔️ Yes, Django signals execute synchronously by default.

**Proof:**

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver
import time

@receiver(pre_save)
def blocking_handler(sender, **kwargs):
    print("Signal handler START - about to sleep for 2 seconds")
    time.sleep(2)  # Blocking call
    print("Signal handler END")

# When you call model.save(), execution will block for 2 seconds
# proving synchronous execution
```

---

### 🧵 Question 2: Thread Behavior

**Do Django signals run in the same thread as the caller?**  
✔️ Yes, signals run in the same thread as the caller.

**Proof:**

```python
import threading
from django.dispatch import Signal
from django.dispatch import receiver

test_signal = Signal()

@receiver(test_signal)
def thread_handler(sender, **kwargs):
    print(f"Handler thread: {threading.current_thread().name}")

# Trigger signal
print(f"Caller thread: {threading.current_thread().name}")
test_signal.send(sender=None)
# Output shows both print same thread name
```

---

### 🔁 Question 3: Transaction Handling

**Do Django signals run in the same database transaction as the caller?**  
✔️ Yes, signals participate in the same transaction when called within an atomic block.

**Proof:**

```python
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def transaction_handler(sender, **kwargs):
    print(f"In transaction: {transaction.get_autocommit()}")

# Outside transaction
some_model.save()  # Output: In transaction: True

# Inside transaction
with transaction.atomic():
    some_model.save()  # Output: In transaction: False
```

---

## 📦 Part 2: Python Custom Iterable Class - Rectangle

### Features:

- Initialize with length and width
- Iteration yields length then width as dictionaries
- Clean string representation

### Code:

```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index == 0:
            self._iter_index += 1
            return {'length': self.length}
        elif self._iter_index == 1:
            self._iter_index += 1
            return {'width': self.width}
        raise StopIteration

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
```

### Usage Example:

```python
rect = Rectangle(5, 10)
print(rect)  # Output: Rectangle(length=5, width=10)

for dimension in rect:
    print(dimension)
# Output:
# {'length': 5}
# {'width': 10}
```

---

## ⚙️ Setup and Running

### Django Signals Project

1. Create and activate virtual environment  
2. Install dependencies: `pip install django`  
3. Run migrations: `python manage.py migrate`  
4. Start server: `python manage.py runserver`  
5. Visit: [http://127.0.0.1:8000/test-signals/](http://127.0.0.1:8000/test-signals/)

### Rectangle Class

Simply import the `Rectangle` class from `rectangle.py` and use as shown above.

---

## 📌 Key Findings

### Django Signals:
- ✅ Execute synchronously by default  
- ✅ Run in the same thread as the caller  
- ✅ Participate in the caller's transaction context  

### Rectangle Class:
- ✅ Clean implementation of Python iteration protocol  
- ✅ Provides dictionary output for each dimension  
- ✅ Easy to extend with additional functionality  

---

## 📄 License

**MIT License** – Free to use and modify.

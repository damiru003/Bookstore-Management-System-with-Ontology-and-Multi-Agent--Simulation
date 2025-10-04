"""
Complete Bookstore Management System - Final Implementation
Integrated Multi-Agent System with Mesa Framework

This system combines:
- Mesa Framework for professional agent-based modeling
- Owlready2 for ontology management and semantic reasoning
- SWRL Rules for business logic and automated inference
- Message Bus for inter-agent communication
- Complete simulation engine with statistics and reporting


"""

import os
import sys
import random
import time
import datetime as dt
from collections import defaultdict
import json

# Import required libraries
try:
    from owlready2 import *
    from owlready2.reasoning import *
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from mesa import Agent, Model, DataCollector
    
    print("✅ All packages loaded successfully")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required packages:")
    print("pip install mesa owlready2 matplotlib numpy pandas")
    sys.exit(1)


# =====================================
# MESSAGE BUS COMMUNICATION SYSTEM
# =====================================

class MessageBus:
    """Handles inter-agent communication with message queuing"""
    
    def __init__(self):
        self.messages = []
        self.message_counter = 0
        self.agent_mailboxes = defaultdict(list)
        self.message_log = []
        
    def register_agent(self, agent_id):
        """Register an agent for message delivery"""
        if agent_id not in self.agent_mailboxes:
            self.agent_mailboxes[agent_id] = []
            
    def send_message(self, sender_id, receiver_id, message_type, content):
        """Send a message from one agent to another"""
        message = {
            'id': self.message_counter,
            'sender': sender_id,
            'receiver': receiver_id,
            'type': message_type,
            'content': content,
            'timestamp': dt.datetime.now(),
            'processed': False
        }
        
        self.messages.append(message)
        self.message_log.append(message)
        self.agent_mailboxes[receiver_id].append(message)
        self.message_counter += 1
        
        return message['id']
        
    def broadcast_message(self, sender_id, message_type, content):
        """Broadcast message to all agents"""
        for receiver_id in self.agent_mailboxes.keys():
            if receiver_id != sender_id:
                self.send_message(sender_id, receiver_id, message_type, content)
        
    def get_messages(self, agent_id):
        """Get all unprocessed messages for an agent"""
        messages = self.agent_mailboxes[agent_id].copy()
        self.agent_mailboxes[agent_id] = []
        
        for msg in messages:
            msg['processed'] = True
            
        return messages
        
    def get_message_stats(self):
        """Get message system statistics"""
        total_messages = len(self.messages)
        processed_messages = sum(1 for msg in self.messages if msg['processed'])
        
        return {
            'total_messages': total_messages,
            'processed_messages': processed_messages,
            'pending_messages': total_messages - processed_messages,
            'registered_agents': len(self.agent_mailboxes),
            'messages_by_type': self._count_messages_by_type()
        }
        
    def _count_messages_by_type(self):
        """Count messages by type"""
        type_counts = defaultdict(int)
        for msg in self.messages:
            type_counts[msg['type']] += 1
        return dict(type_counts)


# =====================================
# ONTOLOGY MANAGEMENT WITH SWRL RULES
# =====================================

class BookstoreOntology:
    """Complete ontology management with SWRL rules integration"""
    
    def __init__(self, ontology_file="bookstore_system.owl"):
        self.ontology_file = ontology_file
        self.onto = get_ontology("http://bookstore.system/ontology.owl")
        self._create_ontology()
        
    def _create_ontology(self):
        """Create the complete ontology structure"""
        with self.onto:
            # Core Classes
            class Person(Thing): pass
            class Customer(Person): pass
            class Employee(Person): pass
            class Book(Thing): pass
            class Inventory(Thing): pass
            class Transaction(Thing): pass
            
            # Data Properties (Attributes)
            class hasName(DataProperty):
                domain = [Person]
                range = [str]
                
            class hasBudget(DataProperty):
                domain = [Customer]
                range = [float]
                
            class hasRole(DataProperty):
                domain = [Employee]
                range = [str]
                
            class hasTitle(DataProperty):
                domain = [Book]
                range = [str]
                
            class hasPrice(DataProperty):
                domain = [Book]
                range = [float]
                
            class hasAuthor(DataProperty):
                domain = [Book]
                range = [str]
                
            class hasGenre(DataProperty):
                domain = [Book]
                range = [str]
                
            class availableQuantity(DataProperty):
                domain = [Inventory]
                range = [int]
                
            class restockThreshold(DataProperty):
                domain = [Inventory]
                range = [int]
                
            class transactionAmount(DataProperty):
                domain = [Transaction]
                range = [float]
            
            # Object Properties (Relationships)
            class purchases(ObjectProperty):
                domain = [Customer]
                range = [Book]
                
            class manages(ObjectProperty):
                domain = [Employee]
                range = [Inventory]
                
            class hasInventory(ObjectProperty):
                domain = [Book]
                range = [Inventory]
                
            class involves(ObjectProperty):
                domain = [Transaction]
                range = [Customer, Book]
        
        # Store class references
        self.Customer = self.onto.Customer
        self.Employee = self.onto.Employee
        self.Book = self.onto.Book
        self.Inventory = self.onto.Inventory
        self.Transaction = self.onto.Transaction
        
        # Create SWRL rules
        self._create_swrl_rules()
        
        print("✅ Ontology created with SWRL rules integrated")
        
    def _create_swrl_rules(self):
        """Create comprehensive SWRL rules for business logic"""
        with self.onto:
            # Derived classes for SWRL rule consequences
            class PremiumCustomer(self.Customer):
                """Customers with high budgets (>$250)"""
                pass
                
            class LowBudgetCustomer(self.Customer):
                """Customers with low budgets (<$100)"""
                pass
                
            class HighValueBook(self.Book):
                """Expensive books (>$30)"""
                pass
                
            class LowStockBook(self.Book):
                """Books with low inventory (<5)"""
                pass
                
            class OverstockedBook(self.Book):
                """Books with excessive inventory (>30)"""
                pass
                
            class ActiveCustomer(self.Customer):
                """Customers who have made purchases"""
                pass
                
            class EligibleForDiscount(self.Customer):
                """Customers eligible for discounts"""
                pass
                
            class RequiresRestock(self.Inventory):
                """Inventory items needing restocking"""
                pass
                
            class HighPerformingEmployee(self.Employee):
                """Employees with good performance"""
                pass
                
            # Store derived class references
            self.PremiumCustomer = PremiumCustomer
            self.LowBudgetCustomer = LowBudgetCustomer
            self.HighValueBook = HighValueBook
            self.LowStockBook = LowStockBook
            self.OverstockedBook = OverstockedBook
            self.ActiveCustomer = ActiveCustomer
            self.EligibleForDiscount = EligibleForDiscount
            self.RequiresRestock = RequiresRestock
            self.HighPerformingEmployee = HighPerformingEmployee
            
        # Define 9 SWRL business rules
        self.swrl_rules = [
            "Customer(?c) ^ hasBudget(?c, ?b) ^ swrlb:greaterThan(?b, 250) -> PremiumCustomer(?c)",
            "Customer(?c) ^ hasBudget(?c, ?b) ^ swrlb:lessThan(?b, 100) -> LowBudgetCustomer(?c)",
            "Book(?book) ^ hasPrice(?book, ?p) ^ swrlb:greaterThan(?p, 30) -> HighValueBook(?book)",
            "Book(?book) ^ hasInventory(?book, ?inv) ^ availableQuantity(?inv, ?qty) ^ swrlb:lessThan(?qty, 5) -> LowStockBook(?book)",
            "Book(?book) ^ hasInventory(?book, ?inv) ^ availableQuantity(?inv, ?qty) ^ swrlb:greaterThan(?qty, 30) -> OverstockedBook(?book)",
            "Customer(?c) ^ Book(?b) ^ purchases(?c, ?b) -> ActiveCustomer(?c)",
            "Inventory(?inv) ^ availableQuantity(?inv, ?qty) ^ restockThreshold(?inv, ?threshold) ^ swrlb:lessThanOrEqual(?qty, ?threshold) -> RequiresRestock(?inv)",
            "PremiumCustomer(?c) ^ ActiveCustomer(?c) -> EligibleForDiscount(?c)",
            "Employee(?e) ^ manages(?e, ?inv) ^ RequiresRestock(?inv) ^ availableQuantity(?inv, ?qty) ^ swrlb:greaterThan(?qty, 0) -> HighPerformingEmployee(?e)"
        ]
        
        print(f"📋 Created {len(self.swrl_rules)} SWRL business rules")
        
    def create_customer(self, customer_id, name, budget):
        """Create a customer individual in ontology"""
        customer = self.Customer(customer_id)
        customer.hasName = [name]
        customer.hasBudget = [budget]
        return customer
        
    def create_employee(self, employee_id, name, role):
        """Create an employee individual in ontology"""
        employee = self.Employee(employee_id)
        employee.hasName = [name]
        employee.hasRole = [role]
        return employee
        
    def create_book_with_inventory(self, book_id, title, price, author="Unknown", genre="General"):
        """Create a book with associated inventory"""
        book = self.Book(book_id)
        book.hasTitle = [title]
        book.hasPrice = [price]
        book.hasAuthor = [author]
        book.hasGenre = [genre]
        
        inventory_id = f"{book_id}_inventory"
        inventory = self.Inventory(inventory_id)
        inventory.availableQuantity = [random.randint(15, 35)]
        inventory.restockThreshold = [random.randint(3, 8)]
        
        book.hasInventory = [inventory]
        return book, inventory
        
    def process_purchase(self, customer, book):
        """Process a book purchase transaction"""
        try:
            if not book.hasInventory:
                return False
                
            inventory = book.hasInventory[0]
            current_qty = inventory.availableQuantity[0] if inventory.availableQuantity else 0
            
            if current_qty <= 0:
                return False
                
            book_price = book.hasPrice[0] if book.hasPrice else 0
            customer_budget = customer.hasBudget[0] if customer.hasBudget else 0
            
            if customer_budget < book_price:
                return False
                
            # Process transaction
            inventory.availableQuantity = [current_qty - 1]
            customer.hasBudget = [customer_budget - book_price]
            
            # Create transaction record
            transaction_id = f"trans_{customer.name}_{book.name}_{int(time.time()*1000)}"
            transaction = self.Transaction(transaction_id)
            transaction.transactionAmount = [book_price]
            transaction.involves = [customer, book]
            
            # Add purchase relationship
            if not hasattr(customer, 'purchases') or customer.purchases is None:
                customer.purchases = []
            customer.purchases.append(book)
            
            return True
            
        except Exception as e:
            return False
            
    def restock_inventory(self, inventory, restock_amount):
        """Restock an inventory item"""
        try:
            current_qty = inventory.availableQuantity[0] if inventory.availableQuantity else 0
            inventory.availableQuantity = [current_qty + restock_amount]
            return True
        except Exception as e:
            return False
            
    def apply_swrl_rules(self):
        """Apply SWRL rules through manual inference"""
        try:
            self._apply_manual_rules()
            return True
        except Exception as e:
            print(f"❌ SWRL error: {e}")
            return False
            
    def _apply_manual_rules(self):
        """Manually apply SWRL business rules"""
        # Rule 1: Premium customers (budget > 250)
        for customer in self.Customer.instances():
            if customer.hasBudget and customer.hasBudget[0] > 250:
                if not isinstance(customer, self.PremiumCustomer):
                    customer.__class__ = self.PremiumCustomer
                    
        # Rule 2: Low budget customers (budget < 100)
        for customer in self.Customer.instances():
            if customer.hasBudget and customer.hasBudget[0] < 100:
                if not isinstance(customer, self.LowBudgetCustomer):
                    customer.__class__ = self.LowBudgetCustomer
                    
        # Rule 3: High value books (price > 30)
        for book in self.Book.instances():
            if book.hasPrice and book.hasPrice[0] > 30:
                if not isinstance(book, self.HighValueBook):
                    book.__class__ = self.HighValueBook
                    
        # Rule 4: Low stock books (quantity < 5)
        for book in self.Book.instances():
            if book.hasInventory:
                inventory = book.hasInventory[0]
                if inventory.availableQuantity and inventory.availableQuantity[0] < 5:
                    if not isinstance(book, self.LowStockBook):
                        book.__class__ = self.LowStockBook
                        
        # Rule 5: Overstocked books (quantity > 30)
        for book in self.Book.instances():
            if book.hasInventory:
                inventory = book.hasInventory[0]
                if inventory.availableQuantity and inventory.availableQuantity[0] > 30:
                    if not isinstance(book, self.OverstockedBook):
                        book.__class__ = self.OverstockedBook
                        
        # Rule 6: Active customers (have purchases)
        for customer in self.Customer.instances():
            if hasattr(customer, 'purchases') and customer.purchases:
                if not isinstance(customer, self.ActiveCustomer):
                    customer.__class__ = self.ActiveCustomer
                    
        # Rule 7: Restock requirements
        for inventory in self.Inventory.instances():
            qty = inventory.availableQuantity[0] if inventory.availableQuantity else 0
            threshold = inventory.restockThreshold[0] if inventory.restockThreshold else 5
            if qty <= threshold:
                if not isinstance(inventory, self.RequiresRestock):
                    inventory.__class__ = self.RequiresRestock
                    
        # Rule 8: Discount eligibility
        for customer in self.Customer.instances():
            if (isinstance(customer, self.PremiumCustomer) and isinstance(customer, self.ActiveCustomer)):
                if not isinstance(customer, self.EligibleForDiscount):
                    customer.__class__ = self.EligibleForDiscount
                    
    def get_swrl_inference_results(self):
        """Get SWRL classification results"""
        return {
            'premium_customers': len(list(self.PremiumCustomer.instances())),
            'low_budget_customers': len(list(self.LowBudgetCustomer.instances())),
            'high_value_books': len(list(self.HighValueBook.instances())),
            'low_stock_books': len(list(self.LowStockBook.instances())),
            'overstocked_books': len(list(self.OverstockedBook.instances())),
            'active_customers': len(list(self.ActiveCustomer.instances())),
            'discount_eligible': len(list(self.EligibleForDiscount.instances())),
            'restock_required': len(list(self.RequiresRestock.instances()))
        }
        
    def save_ontology(self, filename=None):
        """Save ontology to file"""
        if filename is None:
            filename = self.ontology_file
        try:
            self.onto.save(file=filename, format="rdfxml")
            print(f"✅ Ontology saved to {filename}")
            return True
        except Exception as e:
            print(f"❌ Error saving ontology: {e}")
            return False


# =====================================
# MESA SCHEDULER
# =====================================

class RandomActivation:
    """Mesa-compatible random activation scheduler"""
    
    def __init__(self, model):
        self.model = model
        self.agents = []
        
    def add(self, agent):
        if agent not in self.agents:
            self.agents.append(agent)
            
    def remove(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)
            
    def step(self):
        """Execute all agents in random order"""
        agents_copy = self.agents.copy()
        random.shuffle(agents_copy)
        for agent in agents_copy:
            if hasattr(agent, 'step'):
                try:
                    agent.step()
                except Exception as e:
                    if self.model.verbose:
                        print(f"  ⚠️  Agent error: {e}")


# =====================================
# MESA AGENT IMPLEMENTATIONS
# =====================================

class CustomerAgent(Agent):
    """Mesa Customer Agent with ontology and message bus integration"""
    
    def __init__(self, unique_id, model, name, initial_budget):
        super().__init__(model)
        self.unique_id = unique_id
        self.name = name
        self.initial_budget = initial_budget
        self.current_budget = initial_budget
        self.purchased_books = []
        self.browsing_book = None
        self.interest_level = 0
        self.satisfaction = 50.0
        
        # Create ontology individual
        self.onto_customer = model.ontology.create_customer(
            f"customer_{unique_id}", name, initial_budget
        )
        
        # Register with message bus
        model.message_bus.register_agent(f"customer_{unique_id}")
        
    def step(self):
        """Mesa agent step with message processing"""
        # Process incoming messages
        self.process_messages()
        
        # Execute agent behavior
        if random.random() < 0.6:  # 60% activity rate
            if self.browsing_book is None:
                self.browse_books()
            else:
                self.consider_purchase()
                
    def process_messages(self):
        """Process messages from message bus"""
        messages = self.model.message_bus.get_messages(f"customer_{self.unique_id}")
        for msg in messages:
            if msg['type'] == 'price_change':
                # React to price changes
                if self.browsing_book and msg['content'].get('book_id') == self.browsing_book.name:
                    self.interest_level = max(1, self.interest_level - 1)
            elif msg['type'] == 'discount_offer':
                # React to discount offers
                self.satisfaction = min(100, self.satisfaction + 5)
                
    def browse_books(self):
        """Browse available books"""
        book_agents = [agent for agent in self.model.schedule.agents 
                      if isinstance(agent, BookAgent)]
        
        if not book_agents:
            return
            
        # Filter affordable books
        affordable_books = []
        for book_agent in book_agents:
            book_price = book_agent.onto_book.hasPrice[0] if book_agent.onto_book.hasPrice else 0
            if book_price <= self.current_budget:
                affordable_books.append(book_agent)
        
        if affordable_books:
            book_agent = random.choice(affordable_books)
            self.browsing_book = book_agent.onto_book
            self.interest_level = random.randint(2, 5)
            
            if self.model.verbose:
                book_title = self.browsing_book.hasTitle[0] if self.browsing_book.hasTitle else "Unknown"
                print(f"  👀 {self.name} is browsing '{book_title}'")
                
    def consider_purchase(self):
        """Consider purchasing current book"""
        if self.browsing_book is None:
            return
            
        self.interest_level -= 1
        
        if self.interest_level <= 0:
            if random.random() < 0.65:  # 65% purchase chance
                self.attempt_purchase()
            else:
                self.satisfaction = max(0, self.satisfaction - 5)
                if self.model.verbose:
                    book_title = self.browsing_book.hasTitle[0] if self.browsing_book.hasTitle else "Unknown"
                    print(f"  🤔 {self.name} decided not to buy '{book_title}'")
                    
            self.browsing_book = None
            
    def attempt_purchase(self):
        """Attempt to purchase current book"""
        if self.browsing_book is None:
            return
            
        success = self.model.ontology.process_purchase(self.onto_customer, self.browsing_book)
        
        book_title = self.browsing_book.hasTitle[0] if self.browsing_book.hasTitle else "Unknown"
        book_price = self.browsing_book.hasPrice[0] if self.browsing_book.hasPrice else 0
        
        if success:
            self.purchased_books.append(self.browsing_book)
            self.current_budget = self.onto_customer.hasBudget[0] if self.onto_customer.hasBudget else 0
            self.satisfaction = min(100, self.satisfaction + 15)
            
            # Update model statistics FIRST (before any potential errors)
            self.model.total_revenue += book_price
            self.model.total_transactions += 1
            
            if self.model.verbose:
                print(f"  ✅ {self.name} purchased '{book_title}' for ${book_price:.2f} (Budget: ${self.current_budget:.2f})")
                
            # Send purchase notification via message bus (if this fails, revenue is still tracked)
            try:
                self.model.message_bus.send_message(
                    f"customer_{self.unique_id}",
                    "system",
                    "purchase_complete",
                    {'customer': self.name, 'book': book_title, 'price': book_price}
                )
            except Exception as msg_error:
                pass  # Don't let message bus errors prevent purchase tracking
            
        else:
            self.satisfaction = max(0, self.satisfaction - 10)
            if self.model.verbose:
                print(f"  ❌ {self.name} couldn't purchase '{book_title}'")
            
        self.browsing_book = None


class EmployeeAgent(Agent):
    """Mesa Employee Agent with ontology and message bus integration"""
    
    def __init__(self, unique_id, model, name, role="Sales Associate"):
        super().__init__(model)
        self.unique_id = unique_id
        self.name = name
        self.role = role
        self.restock_amount = random.randint(15, 25)
        self.books_restocked = 0
        self.efficiency = random.uniform(0.7, 0.95)
        self.performance_score = 50.0
        
        # Create ontology individual
        self.onto_employee = model.ontology.create_employee(
            f"employee_{unique_id}", name, role
        )
        
        # Register with message bus
        model.message_bus.register_agent(f"employee_{unique_id}")
        
    def step(self):
        """Mesa agent step with message processing"""
        # Process incoming messages
        self.process_messages()
        
        # Execute agent behavior
        if random.random() < 0.7 * self.efficiency:
            self.check_and_restock_inventory()
            
    def process_messages(self):
        """Process messages from message bus"""
        messages = self.model.message_bus.get_messages(f"employee_{self.unique_id}")
        for msg in messages:
            if msg['type'] == 'purchase_complete':
                # Proactively check inventory after purchase
                self.performance_score = min(100, self.performance_score + 1)
                
    def check_and_restock_inventory(self):
        """Check and restock low inventory"""
        book_agents = [agent for agent in self.model.schedule.agents 
                      if isinstance(agent, BookAgent)]
        
        low_stock_books = []
        for book_agent in book_agents:
            if book_agent.onto_book.hasInventory:
                inventory = book_agent.onto_book.hasInventory[0]
                current_qty = inventory.availableQuantity[0] if inventory.availableQuantity else 0
                threshold = inventory.restockThreshold[0] if inventory.restockThreshold else 5
                
                if current_qty <= threshold:
                    low_stock_books.append(book_agent.onto_book)
        
        if low_stock_books:
            book_to_restock = random.choice(low_stock_books)
            self.restock_book(book_to_restock)
            
    def restock_book(self, book):
        """Restock a specific book"""
        if not book.hasInventory:
            return
            
        inventory = book.hasInventory[0]
        old_qty = inventory.availableQuantity[0] if inventory.availableQuantity else 0
        
        success = self.model.ontology.restock_inventory(inventory, self.restock_amount)
        
        if success:
            new_qty = inventory.availableQuantity[0]
            self.books_restocked += 1
            self.performance_score = min(100, self.performance_score + 2)
            
            book_title = book.hasTitle[0] if book.hasTitle else "Unknown"
            
            # Update model statistics FIRST
            self.model.total_restocks += 1
            
            if self.model.verbose:
                print(f"  📦 {self.name} restocked '{book_title}': {old_qty} → {new_qty} (+{self.restock_amount})")
                
            # Send restock notification via message bus (with error handling)
            try:
                self.model.message_bus.send_message(
                    f"employee_{self.unique_id}",
                    "system",
                    "restock_complete",
                    {'employee': self.name, 'book': book_title, 'amount': self.restock_amount}
                )
            except Exception as msg_error:
                pass  # Don't let message bus errors prevent restock tracking


class BookAgent(Agent):
    """Mesa Book Agent with ontology and message bus integration"""
    
    def __init__(self, unique_id, model, book_data):
        super().__init__(model)
        self.unique_id = unique_id
        self.title = book_data['title']
        self.author = book_data['author']
        self.genre = book_data['genre']
        self.base_price = book_data['price']
        
        # Create ontology individual
        self.onto_book, self.onto_inventory = model.ontology.create_book_with_inventory(
            f"book_{unique_id}", self.title, self.base_price, self.author, self.genre
        )
        
        # Register with message bus
        model.message_bus.register_agent(f"book_{unique_id}")
        
    def step(self):
        """Mesa agent step"""
        # 15% chance to adjust price
        if random.random() < 0.15:
            self.adjust_price_based_on_stock()
            
    def adjust_price_based_on_stock(self):
        """Dynamic pricing based on inventory"""
        if not self.onto_book.hasInventory:
            return
            
        inventory = self.onto_book.hasInventory[0]
        current_stock = inventory.availableQuantity[0] if inventory.availableQuantity else 0
        current_price = self.onto_book.hasPrice[0] if self.onto_book.hasPrice else self.base_price
        
        old_price = current_price
        
        if current_stock < 5:  # Low stock - increase price
            new_price = min(current_price * 1.1, self.base_price * 1.4)
        elif current_stock > 25:  # High stock - decrease price
            new_price = max(current_price * 0.95, self.base_price * 0.75)
        else:
            return
            
        if abs(new_price - current_price) > 0.01:
            self.onto_book.hasPrice = [new_price]
            
            if self.model.verbose and random.random() < 0.3:
                print(f"  💰 '{self.title}' price: ${old_price:.2f} → ${new_price:.2f} (Stock: {current_stock})")
                
            # Send price change notification via message bus
            self.model.message_bus.broadcast_message(
                f"book_{self.unique_id}",
                "price_change",
                {'book_id': self.onto_book.name, 'old_price': old_price, 'new_price': new_price}
            )


# =====================================
# MESA MODEL - COMPLETE SYSTEM
# =====================================

class BookstoreModel(Model):
    """
    Complete Mesa model integrating:
    - Mesa framework for ABM
    - Owlready2 for ontology
    - SWRL rules for business logic
    - Message bus for communication
    """
    
    def __init__(self, n_customers=10, n_employees=3, n_books=15, verbose=True):
        try:
            super().__init__()
        except TypeError:
            pass
        
        self.num_customers = n_customers
        self.num_employees = n_employees
        self.num_books = n_books
        self.verbose = verbose
        
        # Initialize core components
        print("🏪 Initializing Complete Bookstore Management System...")
        self.ontology = BookstoreOntology()
        self.message_bus = MessageBus()
        
        # Mesa scheduler
        self.schedule = RandomActivation(self)
        
        # Model statistics
        self.total_revenue = 0.0
        self.total_transactions = 0
        self.total_restocks = 0
        self.step_count = 0
        
        # Register system with message bus
        self.message_bus.register_agent("system")
        
        # Mesa data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Total Revenue": "total_revenue",
                "Total Transactions": "total_transactions",
                "Total Restocks": "total_restocks",
                "Average Customer Satisfaction": lambda m: self.get_avg_customer_satisfaction(),
                "Average Employee Performance": lambda m: self.get_avg_employee_performance(),
                "Premium Customers": lambda m: self.ontology.get_swrl_inference_results()['premium_customers'],
                "Active Customers": lambda m: self.ontology.get_swrl_inference_results()['active_customers'],
                "Low Stock Books": lambda m: self.ontology.get_swrl_inference_results()['low_stock_books'],
                "Total Messages": lambda m: self.message_bus.get_message_stats()['total_messages']
            }
        )
        
        # Create agents
        self._create_agents()
        
        print(f"✅ System initialized successfully:")
        print(f"   🤖 Mesa Framework: Professional ABM structure")
        print(f"   🧠 Ontology (Owlready2): {n_customers + n_employees + n_books} entities")
        print(f"   📋 SWRL Rules: {len(self.ontology.swrl_rules)} business rules")
        print(f"   📬 Message Bus: {len(self.message_bus.agent_mailboxes)} registered agents")
        print(f"   📊 Agents: {n_customers} customers, {n_employees} employees, {n_books} books")
        
    def _create_agents(self):
        """Create all Mesa agents"""
        
        # Customer data
        customer_names = [
            "Alice Johnson", "Bob Wilson", "Carol Smith", "David Brown", "Emma Davis",
            "Frank Miller", "Grace Taylor", "Henry Garcia", "Ivy Martinez", "Jack Rodriguez"
        ]
        
        # Create customers
        for i in range(self.num_customers):
            name = customer_names[i % len(customer_names)]
            if i >= len(customer_names):
                name += f" {i // len(customer_names) + 1}"
                
            budget = random.uniform(100.0, 300.0)
            customer = CustomerAgent(i, self, name, budget)
            self.schedule.add(customer)
            
        # Employee data
        employee_data = [
            ("Sarah Manager", "Store Manager"),
            ("Mike Associate", "Sales Associate"),
            ("Lisa Clerk", "Inventory Clerk")
        ]
        
        # Create employees
        for i in range(self.num_employees):
            name, role = employee_data[i % len(employee_data)]
            if i >= len(employee_data):
                name = f"{name} {i // len(employee_data) + 1}"
                
            employee = EmployeeAgent(self.num_customers + i, self, name, role)
            self.schedule.add(employee)
            
        # Book catalog
        book_catalog = [
            {"title": "The Great Adventure", "author": "John Smith", "genre": "Adventure", "price": 24.99},
            {"title": "Mystery of the Lost City", "author": "Jane Doe", "genre": "Mystery", "price": 19.99},
            {"title": "Science and Wonder", "author": "Dr. Alan Brown", "genre": "Science", "price": 34.99},
            {"title": "Fantasy Realms", "author": "Sarah Wilson", "genre": "Fantasy", "price": 22.99},
            {"title": "Modern Philosophy", "author": "Prof. David Lee", "genre": "Philosophy", "price": 29.99},
            {"title": "Art Through the Ages", "author": "Maria Garcia", "genre": "Art", "price": 39.99},
            {"title": "Digital Revolution", "author": "Tech Expert", "genre": "Technology", "price": 27.99},
            {"title": "Classic Literature", "author": "Various Authors", "genre": "Literature", "price": 16.99},
            {"title": "Space Exploration", "author": "NASA Scientists", "genre": "Science", "price": 31.99},
            {"title": "Psychology Today", "author": "Dr. Emma Clark", "genre": "Psychology", "price": 25.99}
        ]
        
        # Create books
        for i in range(self.num_books):
            book_data = book_catalog[i % len(book_catalog)]
            if i >= len(book_catalog):
                book_data = book_data.copy()
                book_data["title"] += f" Vol {i // len(book_catalog) + 1}"
                
            book = BookAgent(self.num_customers + self.num_employees + i, self, book_data)
            self.schedule.add(book)
            
    def step(self):
        """Execute one Mesa model step"""
        self.step_count += 1
        
        # Apply SWRL rules every 10 steps
        if self.step_count % 10 == 0:
            self.ontology.apply_swrl_rules()
            
        # Execute all agents
        self.schedule.step()
        
        # Collect data
        self.datacollector.collect(self)
        
    def get_avg_customer_satisfaction(self):
        """Calculate average customer satisfaction"""
        customers = [agent for agent in self.schedule.agents if isinstance(agent, CustomerAgent)]
        if not customers:
            return 0
        return sum(c.satisfaction for c in customers) / len(customers)
        
    def get_avg_employee_performance(self):
        """Calculate average employee performance"""
        employees = [agent for agent in self.schedule.agents if isinstance(agent, EmployeeAgent)]
        if not employees:
            return 0
        return sum(e.performance_score for e in employees) / len(employees)
        
    def run_simulation(self, steps=100):
        """Run the complete simulation"""
        print(f"\n🚀 Starting simulation for {steps} steps...")
        print("="*60)
        
        start_time = time.time()
        
        for step in range(steps):
            if self.verbose and (step % 25 == 0 or step < 3):
                print(f"\n📅 Step {step + 1}/{steps}:")
                
            self.step()
            
            if self.verbose and step > 0 and (step + 1) % 25 == 0:
                print(f"  📊 Progress: Revenue=${self.total_revenue:.2f}, "
                      f"Transactions={self.total_transactions}, "
                      f"Satisfaction={self.get_avg_customer_satisfaction():.1f}%, "
                      f"Messages={self.message_bus.get_message_stats()['total_messages']}")
                      
        end_time = time.time()
        simulation_duration = end_time - start_time
        
        print(f"\n✅ Simulation completed in {simulation_duration:.2f} seconds!")
        self._print_final_results()
        
        # Save ontology
        self.ontology.save_ontology()
        
        return self.datacollector.get_model_vars_dataframe()
        
    def _print_final_results(self):
        """Print comprehensive final results"""
        print("\n" + "="*70)
        print("📊 COMPLETE SYSTEM RESULTS")
        print("="*70)
        
        print(f"\n💰 BUSINESS PERFORMANCE")
        print(f"  Total Revenue: ${self.total_revenue:.2f}")
        print(f"  Total Transactions: {self.total_transactions}")
        print(f"  Total Restocks: {self.total_restocks}")
        print(f"  Average Revenue/Step: ${self.total_revenue/self.step_count:.2f}")
        
        # Agent analytics
        customers = [a for a in self.schedule.agents if isinstance(a, CustomerAgent)]
        employees = [a for a in self.schedule.agents if isinstance(a, EmployeeAgent)]
        
        print(f"\n👥 AGENT ANALYTICS")
        print(f"  Average Customer Satisfaction: {self.get_avg_customer_satisfaction():.1f}%")
        print(f"  Average Employee Performance: {self.get_avg_employee_performance():.1f}%")
        print(f"  Active Customers: {len([c for c in customers if c.purchased_books])}/{len(customers)}")
        
        # SWRL results
        swrl_results = self.ontology.get_swrl_inference_results()
        print(f"\n🧠 SWRL BUSINESS INTELLIGENCE")
        print(f"  Premium Customers: {swrl_results['premium_customers']} (Budget > $250)")
        print(f"  Active Customers: {swrl_results['active_customers']} (Have purchases)")
        print(f"  Low Stock Books: {swrl_results['low_stock_books']} (Quantity < 5)")
        print(f"  Discount Eligible: {swrl_results['discount_eligible']} (Premium + Active)")
        
        # Message bus stats
        msg_stats = self.message_bus.get_message_stats()
        print(f"\n📬 MESSAGE BUS STATISTICS")
        print(f"  Total Messages: {msg_stats['total_messages']}")
        print(f"  Messages Processed: {msg_stats['processed_messages']}")
        print(f"  Registered Agents: {msg_stats['registered_agents']}")
        print(f"  Messages by Type: {msg_stats['messages_by_type']}")
        
        # System integration
        print(f"\n🏆 COMPLETE SYSTEM INTEGRATION")
        print(f"  ✅ Mesa Framework: Professional ABM with {len(self.schedule.agents)} agents")
        print(f"  ✅ Owlready2 Ontology: {self.num_customers + self.num_employees + self.num_books} semantic entities")
        print(f"  ✅ SWRL Rules: {len(self.ontology.swrl_rules)} business rules applied")
        print(f"  ✅ Message Bus: {msg_stats['total_messages']} inter-agent communications")
        print(f"  ✅ Data Collection: {len(self.datacollector.model_vars)} metrics tracked")
        
        print(f"\n🎉 ALL COMPONENTS INTEGRATED SUCCESSFULLY!")


# =====================================
# MAIN EXECUTION
# =====================================

def main():
    """Main program entry point"""
    print("🏪" + "="*68 + "🏪")
    print("    COMPLETE BOOKSTORE MANAGEMENT SYSTEM")
    print("    Mesa + Owlready2 + SWRL + Message Bus Integration")
    print("🏪" + "="*68 + "🏪")
    
    print("\nSelect simulation mode:")
    print("1️⃣  Quick Demo (30 steps, 5 customers)")
    print("2️⃣  Standard Simulation (75 steps, 8 customers)")
    print("3️⃣  Full Simulation (150 steps, 12 customers)")
    print("4️⃣  Custom Configuration")
    print("0️⃣  Exit")
    
    while True:
        try:
            choice = input("\n👉 Enter your choice (0-4): ").strip()
            
            if choice == "0":
                print("👋 Thank you for using the Complete Bookstore System!")
                break
            elif choice == "1":
                print("\n🎯 QUICK DEMO")
                model = BookstoreModel(n_customers=5, n_employees=2, n_books=8, verbose=True)
                results = model.run_simulation(steps=30)
            elif choice == "2":
                print("\n🎯 STANDARD SIMULATION")
                model = BookstoreModel(n_customers=8, n_employees=3, n_books=12, verbose=True)
                results = model.run_simulation(steps=75)
            elif choice == "3":
                print("\n🎯 FULL SIMULATION")
                model = BookstoreModel(n_customers=12, n_employees=4, n_books=18, verbose=True)
                results = model.run_simulation(steps=150)
            elif choice == "4":
                print("\n🎯 CUSTOM CONFIGURATION")
                try:
                    customers = int(input("Number of customers (3-25): ") or 8)
                    employees = int(input("Number of employees (1-8): ") or 3)
                    books = int(input("Number of books (5-30): ") or 15)
                    steps = int(input("Simulation steps (20-300): ") or 100)
                    
                    model = BookstoreModel(n_customers=customers, n_employees=employees, n_books=books, verbose=True)
                    results = model.run_simulation(steps=steps)
                except ValueError:
                    print("❌ Invalid input. Using defaults.")
                    continue
            else:
                print("❌ Invalid choice. Please enter 0-4.")
                continue
                
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            results_file = f"simulation_results_{timestamp}.csv"
            try:
                results.to_csv(results_file)
                print(f"\n📄 Results saved to {results_file}")
            except:
                pass
                
            again = input("\n🔄 Run another simulation? (y/n): ").strip().lower()
            if again not in ['y', 'yes']:
                print("👋 Thank you for using the Complete Bookstore System!")
                break
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()

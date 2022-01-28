import unittest
from datetime import datetime, timedelta
from surfshop import CheckoutDateError, TooManyBoardsError, ShoppingCart


class surfshopTest(unittest.TestCase):
  def setUp(self):
    self.cart = ShoppingCart()
  
  def test_addsurfboards(self):
    for quantity in [2, 1, 4]:
      print(quantity)
      with self.subTest(quantity=quantity):
        suffix = '' if quantity == 1 else 's'
        message = f'Successfully added {quantity} surfboard{suffix} to cart!'
        self.assertEqual(self.cart.add_surfboards(quantity), message)
        
  def test_too_many_boards_error(self):
    with self.assertRaises(TooManyBoardsError):
      self.cart.add_surfboards(5)

  def test_apply_locals_discount(self):
    self.assertEquals(self.cart.locals_discount, False)
    self.cart.apply_locals_discount()
    self.assertEquals(self.cart.locals_discount, True)

  def test_checkout_date(self):
    for day in [0.00001, 10, 1]:
      with self.subTest(day=day):
        date = datetime.today() + timedelta(days=day) 
        self.cart.set_checkout_date(date)
        self.assertEqual(date, self.cart.checkout_date)

  def test_checkout_date_yesterday(self):
    yesterday = datetime.today() - timedelta(1)
    with self.assertRaises(CheckoutDateError):
      self.cart.set_checkout_date(yesterday)


unittest.main()
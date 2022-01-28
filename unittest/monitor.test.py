import unittest
import monitor

class MonitorTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    cls.monitor1 = monitor.Monitor()

  def test_calculate_remaining_time(self):
    testcases = [10, 1000, 9999, 0, -10]
    results = [(0, 0), (1, 6), (11, 6), (0, 0), (0, 0)]
    for index, kms in enumerate(testcases):
      with self.subTest():
        self.assertEqual(self.monitor1.calculate_remaining_time(kms), results[index], f'expected {kms} kms to equal {results[index]} (hours, minutes)')

  def test_request_flight_attendant(self):
    self.assertWarns(monitor.CustomerRequestWarning)

if __name__ == "__main__":
  unittest.main()
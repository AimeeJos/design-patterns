from abc import ABC, abstractmethod

# Strategy Interface
class ReportStrategy(ABC):
    @abstractmethod
    def generate(self, data, filename):
        pass

# Concrete Strategies
class PDFReportStrategy(ReportStrategy):
    def generate(self, data, filename):
        print(f"Generating PDF report: {filename}.pdf with data: {data}")
        # Actual PDF generation logic would go here

class CSVReportStrategy(ReportStrategy):
    def generate(self, data, filename):
        print(f"Generating CSV report: {filename}.csv with data: {data}")
        # Actual CSV generation logic would go here

class JSONReportStrategy(ReportStrategy):
    def generate(self, data, filename):
        print(f"Generating JSON report: {filename}.json with data: {data}")
        # Actual JSON generation logic would go here

# Context
class ReportGenerator:
    def __init__(self, strategy: ReportStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ReportStrategy):
        self._strategy = strategy

    def generate_report(self, data, filename):
        self._strategy.generate(data, filename)

# Usage Example
if __name__ == "__main__":
    data = {"title": "Sales Report", "content": [100, 200, 300]}
    filename = "sales_report"

    # Choose strategy at runtime
    generator = ReportGenerator(PDFReportStrategy())
    generator.generate_report(data, filename)

    generator.set_strategy(CSVReportStrategy())
    generator.generate_report(data, filename)

    generator.set_strategy(JSONReportStrategy())
    generator.generate_report(data, filename)
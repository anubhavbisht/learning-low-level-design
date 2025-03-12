class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_as_html(self):
        return f"<h1>{self.title}</h1><p>{self.content}</p>"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.format_as_html())


class NewReport:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
class ReportFormatter:
    @staticmethod
    def format_as_html(report):
        return f"<h1>{report.title}</h1><p>{report.content}</p>"

class ReportSaver:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, "w") as f:
            f.write(ReportFormatter.format_as_html(report))

report = Report("Sales Report", "Total revenue: $5000")
ReportSaver.save_to_file(report, "report.html")
        
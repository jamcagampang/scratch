from jinja2 import Template
from sample import report

# Read the local HTML template file
with open('template.html', 'r') as file:
    bootstrap_template = file.read()

# Sample data to populate the template
data = {
    'reports': report
}

# Render the template with the data
template = Template(bootstrap_template)
output_html = template.render(data)

# Output the rendered HTML to a new file
with open('output.html', 'w') as file:
    file.write(output_html)

print("HTML file generated successfully!")
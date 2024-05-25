import textwrap

def format_table(headers, data, col_widths):
    # Calculate max lines needed for each row
    max_lines_per_row = []
    for row in data:
        max_lines = 0
        for i, cell in enumerate(row):
            wrapped = textwrap.wrap(cell, col_widths[i])
            if len(wrapped) > max_lines:
                max_lines = len(wrapped)
        max_lines_per_row.append(max_lines)
    
    # Build the table header
    header_lines = []
    for i, header in enumerate(headers):
        wrapped = textwrap.wrap(header, col_widths[i])
        for line in wrapped:
            header_lines.append(line.ljust(col_widths[i]))
    header_line = ' | '.join(header_lines)
    separator_line = '-+-'.join('-' * width for width in col_widths)
    
    # Build the table row by row
    table_lines = [header_line, separator_line]
    for row, max_lines in zip(data, max_lines_per_row):
        for line_idx in range(max_lines):
            line = []
            for i, cell in enumerate(row):
                wrapped = textwrap.wrap(cell, col_widths[i])
                if line_idx < len(wrapped):
                    line.append(wrapped[line_idx].ljust(col_widths[i]))
                else:
                    line.append(' ' * col_widths[i])
            table_lines.append(' | '.join(line))
    
    return '\n'.join(table_lines)
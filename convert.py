

def convert_seconds(init_seconds):
	seconds_formatted = ""

	# check init_seconds for years
	if init_seconds / 31536000 >= 1:
		years = init_seconds // 31536000

		if years > 1:
			seconds_formatted += f"{years} years, "
		else:
			seconds_formatted += f"{years} year, "

		init_seconds -= years * 31536000
	
	# check init_seconds for months
	if init_seconds / 2628288 >= 1:
		months = init_seconds // 2628288

		if months > 1:
			seconds_formatted += f"{months} months, "
		else:
			seconds_formatted += f"{months} month, "

		init_seconds -= months * 2628288

	# check init_seconds for weeks
	if init_seconds / 604800 >= 1:
		weeks = init_seconds // 604800

		if weeks > 1:
			seconds_formatted += f"{weeks} weeks, "
		else:
			seconds_formatted += f"{weeks} week, "

		init_seconds -= weeks * 604800

	# check init_seconds for days
	if init_seconds / 86400 >= 1:
		days = init_seconds // 86400

		if days > 1:
			seconds_formatted += f"{days} days, "
		else:
			seconds_formatted += f"{days} day, "

		init_seconds -= days * 86400

	# check init_seconds for hours
	if init_seconds / 3600 >= 1:
		hours = init_seconds // 3600

		if hours > 1:
			seconds_formatted += f"{hours} hours, "
		else:
			seconds_formatted += f"{hours} hour, "

		init_seconds -= hours * 3600

	# check init_seconds for minutes
	if init_seconds / 60 >= 1:
		minutes = init_seconds // 60
		
		if minutes > 1:
			seconds_formatted += f"{minutes} minutes, "
		else:
			seconds_formatted += f"{minutes} minute, "

		init_seconds -= minutes * 60

	# check init_seconds for seconds
	if init_seconds >= 1:
		seconds = init_seconds
		
		if seconds > 1:
			seconds_formatted += f"{seconds} seconds, "
		else:
			seconds_formatted += f"{seconds} second, "

		init_seconds -= seconds

	# clean up the end of seconds_formatted
	seconds_formatted = seconds_formatted[:len(seconds_formatted) - 2]

	return seconds_formatted

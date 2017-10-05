# Find the anfle between the two clock hands

# First find the hour degree and minute degree for hour angle from 12

hour_degree = (360 / 12.0)
hr_minutes_degree = (360 / 12 / 60.0)

# hour degree = 30 and hr minutes degree 0.5.
# Find minute angle from 12
minutes_degree = 360 / 60.0
# minute degree is 6
# Now find the angle by using following formula.


print "{} - {} - {}".format(hour_degree, hr_minutes_degree, minutes_degree)


def clockangles(hour, minute):
    ans = abs((
        hour * hour_degree + minute * hr_minutes_degree
    ) - (minute * minutes_degree))
    # for no negative angle
    return min(360 - ans, ans)


print clockangles(12, 30)

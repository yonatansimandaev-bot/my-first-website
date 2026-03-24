import random
from datetime import datetime, timedelta

DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def generate_schedule(tasks):
    schedule = {day: [] for day in DAYS}

    # Separate tasks
    red_black = [t for t in tasks if t['color'] in ['🔴','⚫']]
    yellow = [t for t in tasks if t['color'] == '🟡']
    green = [t for t in tasks if t['color'] == '🟢']

    # STEP 1: Place fixed tasks
    for task in red_black:
        for day in task['days'].split(","):
            schedule[day].append(task)

    # STEP 2: Calculate average duration (yellow tasks only)
    if yellow:
        avg = sum(int(t['duration']) for t in yellow) / len(yellow)
    else:
        avg = 60

    # STEP 3: Create free slots (simple version: whole day)
    free_slots = {day: [(time_to_dt("07:00"), time_to_dt("22:00"))] for day in DAYS}

    # Remove red/black from free slots
    for day in DAYS:
        for task in schedule[day]:
            if task.get("start") and task.get("end"):
                free_slots[day] = cut_slot(free_slots[day],
                                          time_to_dt(task["start"]),
                                          time_to_dt(task["end"]))

    # STEP 4: Schedule yellow tasks
    for task in yellow:
        duration = int(task["duration"])
        range_min = int(avg * 2)
        range_max = int(avg * 3)

        for day in task["days"].split(","):
            slots = free_slots[day]
            random.shuffle(slots)

            for slot in slots:
                slot_len = minutes(slot)
                if slot_len >= duration:
                    offset = random.randint(0, slot_len - duration)
                    start = slot[0] + timedelta(minutes=offset)
                    end = start + timedelta(minutes=duration)

                    task["assigned_day"] = day
                    task["assigned_start"] = dt_to_str(start)
                    task["assigned_end"] = dt_to_str(end)

                    schedule[day].append(task)
                    free_slots[day] = cut_slot(slots, start, end)
                    break
            break

    # STEP 5: Schedule green tasks (fully random)
    for task in green:
        duration = int(task["duration"])
        day = random.choice(DAYS)
        slots = free_slots[day]

        for slot in slots:
            if minutes(slot) >= duration:
                offset = random.randint(0, minutes(slot) - duration)
                start = slot[0] + timedelta(minutes=offset)
                end = start + timedelta(minutes=duration)

                task["assigned_day"] = day
                task["assigned_start"] = dt_to_str(start)
                task["assigned_end"] = dt_to_str(end)

                schedule[day].append(task)
                free_slots[day] = cut_slot(slots, start, end)
                break

    return schedule


# --- Helpers ---
def time_to_dt(t):
    return datetime.strptime(t, "%H:%M")

def dt_to_str(dt):
    return dt.strftime("%H:%M")

def minutes(slot):
    return int((slot[1] - slot[0]).total_seconds() // 60)

def cut_slot(slots, start, end):
    new_slots = []
    for s, e in slots:
        if end <= s or start >= e:
            new_slots.append((s, e))
        else:
            if s < start:
                new_slots.append((s, start))
            if end < e:
                new_slots.append((end, e))
    return new_slots

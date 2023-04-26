import os
from copy import deepcopy
from pelican import signals


def update_person(person, group_name):
    updated_person = deepcopy(person)
    groups = updated_person.groups
    groups = groups.replace(" ", "").split(',')
    indx = groups.index(group_name)
    fields = [updated_person.active, updated_person.type, updated_person.position]
    new_values = []
    for values in fields:
        values = values.split(',') if isinstance(values, str) else values
        if len(values) > 1:
            new_value = values[indx].strip()
        else:
            new_value = values[0]
        new_values.append(new_value)
    updated_person.active = new_values[0]
    updated_person.type = new_values[1]
    updated_person.position = new_values[2]
    return updated_person


def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'update_person': update_person})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)

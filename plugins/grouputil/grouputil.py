import os
from copy import deepcopy
from pelican import signals


def update_members(members, group_name):
    new_members = []
    for updated_person in members:
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
        new_members.append(updated_person)
    return new_members

def update_person(updated_person, group_name):
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

def update_member_position(person_dict, group_name):
    """If a member has more than one position and site group
       this function selects a postion relevant for a given group.
       Was originally implemented to show correct positions in reserch pages
       for people who belong to both DIAG and the CARA Lab
    """
    # If a person has only one group, all positons belong to this group
    # in this case the 'groups' value will be string, check for the
    # list length of 1 is added for robustness
    if len(group_name) == 0:
        return person_dict

    groups = person_dict["groups"]
    if isinstance(groups, str) or (isinstance(groups, list) and len(groups) == 1):
        return person_dict

    person_dict_copy = person_dict.copy()
    indx = groups.index(group_name)
    all_positions = person_dict_copy["position"]
    positions = all_positions.split(',') if isinstance(all_positions, str) else all_positions
    if len(positions) > 1:
        group_position = positions[indx].strip()
    else:
        group_position = positions[0]
    person_dict_copy["position"] = group_position
    return person_dict_copy


def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'update_members': update_members})
    pelican.env.filters.update({'update_person': update_person})
    pelican.env.filters.update({'update_member_position': update_member_position})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)

import rules
from events.models import Event


@rules.predicate
def is_user(user):
    return True

@rules.predicate
def allow_check(user):
    return True

@rules.predicate()
def is_event_creator(user, content):
    print('content', content)
    print('user', user)
    # return content.created_by == user
    # return Event.objects.filter(created_by=user).exists()

@rules.predicate
def can_create_event(user):
    # write some predicate here instead of just returning True
    return True

rules.add_perm('event_app.create_event', is_user)
rules.add_perm('event_app.delete_event', is_event_creator)
rules.add_perm('event_app.list_events', allow_check)
rules.add_perm('event_app.update_event', allow_check)

"""
Example Usage of rules:

@rules.predicate
def is_a_climber(user):
    return Climber.objects.filter(user=user).exists()

@rules.predicate
def is_a_routesetter(user):
    return RouteSetter.objects.filter(user=user).exists()

@rules.predicate
def is_related_to_routesetters_boulder(user, content=None):
    if content is None or not hasattr(content, 'boulder'):
        return False
    return content.boulder.routesetter == user

@rules.predicate
def object_is_none(user, obj=None):
    return obj is None

@rules.predicate
def is_author(user, content):
    if not hasattr(content, 'author'):
        return False
    return content.author == user

rules.add_perm('climb_app.create_boulder', is_a_routesetter)
rules.add_perm('climb_app.retrieve_boulder', is_a_climber | is_a_routesetter & is_author)
rules.add_perm('climb_app.update_boulder', is_a_routesetter & is_author)
rules.add_perm('climb_app.delete_boulder', is_a_routesetter & is_author)
rules.add_perm('climb_app.retrieve_reviews', is_a_routesetter)
rules.add_perm('climb_app.retrieve_climbers', is_a_routesetter)

rules.add_perm('climb_app.create_climber_content', is_a_climber)
rules.add_perm('climb_app.retrieve_climber_content',
               (is_a_climber |
                is_a_routesetter & is_related_to_routesetters_boulder |
                is_a_routesetter & object_is_none))
rules.add_perm('climb_app.update_climber_content', is_a_climber & is_author)
rules.add_perm('climb_app.delete_climber_content', is_a_climber & is_author)
"""
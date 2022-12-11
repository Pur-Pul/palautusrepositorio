class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class Not:
    def __init__(self, condition):
        self._condition = condition
    
    def test(self, player):
        return not self._condition.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        return not HasAtLeast(self._value, self._attr).test(player)


class Or:
    def __init__(self, *conditions):
        self._conditions = conditions

    def test(self, player):
        return_val = False
        for condition in self._conditions:
            return_val = return_val or condition.test(player)
        return return_val


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class QueryBuilder:
    def __init__(self, query = None):
        self.query_object = query
    
    def all(self):
        if self.query_object is not None:
            return QueryBuilder(And(self.query_object, All()))
        else:
            return QueryBuilder(All())
    
    def hasFewerThan(self, value, attr):
        if self.query_object is not None:
            return QueryBuilder(And(self.query_object, HasFewerThan(value, attr)))
        else:
            return QueryBuilder(HasFewerThan(value, attr))
    
    def playsIn(self, team):
        if self.query_object is not None:
            return QueryBuilder(And(self.query_object, PlaysIn(team)))
        else:
            return QueryBuilder(PlaysIn(team))
    
    def hasAtLeast(self, value, attr):
        if self.query_object is not None:
            return QueryBuilder(And(self.query_object, HasAtLeast(value, attr)))
        else:
            return QueryBuilder(HasAtLeast(value, attr))
    
    def oneOf(self, *conditions):
        return QueryBuilder(Or(*conditions))

    def build(self):
        return self.query_object
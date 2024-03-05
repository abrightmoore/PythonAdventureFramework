#   @TheWorldFoundry

class Graph:
    class Node:
        def __init__(self, label, data):
            self.label = label
            self.child = {}
            self.data = data
        
        def add_child(self, child_node):
            self.child[child_node.label] = child_node

    def __init__(self):
        self.nodes = {}
        self.vertices = {}
        self.relations = {}
        
    def list_vertices(self):
        result = []
        for (a,b,c) in self.vertices:
            result.append(a+" --- "+b+" --> "+c+" = "+str(self.vertices[(a,b,c)]))
        return result
    
    def add_node(self, node):
        self.nodes[node.label] = node
    
    def add_vertex(self, source_node, target_node, vertex_label, vertex_value):
        self.add_node(source_node)
        self.add_node(target_node)
        source_node.add_child(target_node)
        self.vertices[(source_node.label, vertex_label, target_node.label)] = vertex_value
        if (source_node.label, target_node.label) in self.relations:
            self.relations[(source_node.label, target_node.label)].append(vertex_label)
        else: 
            self.relations[(source_node.label, target_node.label)] = [vertex_label]


class UI:
    class UI_Output:
        def __init__(self):
            pass
            
        def display_text_lines(self, lines):
            for line in lines:
                print(line)


    class UI_Input:
        def __init__(self):
            pass
            
        def text_input_wait(self, prompt):
            user_input = input(prompt)
            return user_input
    
    def __init__(self):
        self.ui_out = self.UI_Output()
        self.ui_in = self.UI_Input()


class Game:
    KEY_DESC = "description"
    KEY_PROMPT = "prompt"
    STR_SEPERATOR = "_______________________"
    REL_CONTAINS = "contains"

    class Player:
        def __init__(self, location):
            self.location = location
            
    def __init__(self, universe, start_node):
        self.model = universe
        self.view = UI()
        self.players = [ self.Player(start_node) ]
        
    def run(self):
        for player in self.players:
            #   Process the area the player is within (current node)
            self.view.ui_out.display_text_lines([player.location.label])  #  Node player is on
            self.view.ui_out.display_text_lines(player.location.data[self.KEY_DESC])  #  Friendly text description of here
            self.view.ui_out.display_text_lines(self.look(player))  #  What can we see?
            self.view.ui_in.text_input_wait(player.location.data[self.KEY_PROMPT])  #  Prompt for action

    def look(self, player):
        '''
            What can this player see? Get a formatted set of display lines
        '''
        location = player.location
        result = []
        for child_label in location.child:
            # print(child)
            if (location.label, child_label) in self.model.relations:
                vert_label = self.model.relations[(location.label, child_label)]
                for v in vert_label:
                    vert_value = self.model.vertices[(location.label, v, child_label)]
                    result.append(child_label + " " + v + " value is "+str(vert_value))
                # print(vert_label, vert_value)
        return result

            
office = Graph.Node( "Home Office", {})
chair = Graph.Node( "Office Chair", {})
computer = Graph.Node( "Computer", {})
keyboard = Graph.Node( "Computer Keyboard", {})
monitor = Graph.Node( "Computer Monitor", {})
mouse = Graph.Node( "Computer Mouse", {})
desk = Graph.Node( "Wooden Desk", {})
avatar = Graph.Node( "You", {})

game = Game(Graph(), office)
office.data =    {   game.KEY_DESC : [
                        "You sit in a tall fabric chair, using a computer.",
                        "Your arms are carrying the weight of your frame on elbows resting on a hard wood desk.",
                        "Your finger tips lie gently on the keyboard.",
                    game.STR_SEPERATOR ],
                    game.KEY_PROMPT : "What will you do?   "
                }

game.model.add_vertex(office, chair, game.REL_CONTAINS, 1)
game.model.add_vertex(chair, avatar, game.REL_CONTAINS, 1)
game.model.add_vertex(office, desk, game.REL_CONTAINS, 1)
game.model.add_vertex(office, computer, game.REL_CONTAINS, 1)
game.model.add_vertex(desk, monitor, game.REL_CONTAINS, 1)
game.model.add_vertex(desk, keyboard, game.REL_CONTAINS, 1)
game.model.add_vertex(desk, mouse, game.REL_CONTAINS, 1)

for v in game.model.list_vertices():
    print(v)

game.run()
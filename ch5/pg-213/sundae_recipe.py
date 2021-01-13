#sundae_recipe

def make_sundae(ice_cream='vanilla', sauce='chocolate', nuts=True, banana=True, brownies=False, whipped_cream=True):   #parameters are set with default values
    recipe = ice_cream + ' ice cream and ' + sauce + ' sauce '  #This is the first recipe
    if nuts:    #if nuts==True; default is True
        recipe = recipe + 'with nuts and '
    if banana:    #if banana==True; default value is True
        recipe = recipe + 'a banana and '
    if brownies:  #if browniew==True; default value is False
        recipe = recipe + 'a brownie and '
    if not whipped_cream:   #if whipped_cream==False; default is True
        recipe = recipe + 'no '
    recipe = recipe + 'whipped cream on top.'   #new reciped based on the conditionals
    return recipe

#recipe='vanilla ice cream and chocolate sauce' for all default arguments

sundae = make_sundae()   #all defaults values as arguments
print('One sundae coming up with', sundae)

#One sundae coming up with vanilla ice cream and chocolate sauce with nuts and a banana and whipped cream on top

sundae = make_sundae('chocolate')   #All defaults values as arguments except for the first parameter ice_cream; whose argument value would be 'chocolate'
print('One sundae coming up with', sundae)

#One sundae coming up with chocolate ice cream and chocolate sauce with nuts and a banana and whipped cream on top

sundae = make_sundae(sauce='caramel', whipped_cream=False, banana=False)  #default argument values for ice_cream, nuts, brownies and keyword argument for sauce, whipped_cream and banana
print('One sundae coming up with', sundae)

#One sundae coming up with vanilla ice cream and caramel sauce with nuts and no whipped cream on top

sundae = make_sundae(whipped_cream=False, banana=True,brownies=True, ice_cream='peanut butter')    #default argument values for sauce and nuts; keyword arguments for whipped_cream, banana, broenies and ice_cream
print('One sundae coming up with', sundae)

#One sundae coming up with peanut butter ice cream and chocolate sauce with nuts and a banana and a brownie and no whipped cream on top

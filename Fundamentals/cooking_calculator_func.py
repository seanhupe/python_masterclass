turkey_cooking_time = 14
ham_cooking_time = 5

def cooking_end_time(start_time, duration):
    return (start_time + duration) % 24

# print(cooking_end_time(13, 8))
print(f"Take the turkey out of the oven at {cooking_end_time(13, turkey_cooking_time)} o'clock")
print(f"Take the ham out of the oven at {cooking_end_time(13, ham_cooking_time)} o'clock")

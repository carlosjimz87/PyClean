route = {'id': 271, 'title': "Fast Apps"}
query = {'id': 1, 'render_fast': True}
post = {'email': "chars@gmail.com", 'name': "Chars"}

m1 = {**query, ** post, **route}

print(m1)

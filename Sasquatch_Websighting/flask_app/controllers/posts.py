from flask_app.models.post import Post
from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,session,flash


# Create a Post
@app.route('/create_post', methods=['POST'])
def create_a_post():
    if 'user_id' in session:

        if not Post.validate_post(request.form):
            return redirect('/dashboard')
        data = {
                'location' : request.form['location'],
                'date' : request.form['date'],
                'content' : request.form['content'],
                'sasquatches' : request.form['sasquatches'],
                'user_id' : session['user_id']
            }
        Post.save(data)
        return redirect ('/dashboard')
    return redirect('/')

# Get Post by User Id
@app.route('/show/<int:post_id>')
def show_post_by_post_id(post_id):
    if 'user_id' not in session:
        return redirect('/')
    return render_template('show.html', 
    user = User.getById({'id': session['user_id']}),
    post = Post.getById_w_user({'post_id' : post_id}))

# Update Post
@app.route('/edit/<int:post_id>')
def update_post(post_id):
    if 'user_id' not in session:
        return redirect('/')

    return render_template('edit.html', 
        user = User.getById({'id': session['user_id']}), 
        post = Post.getById_w_user({'post_id' : post_id}))

@app.route('/update_post/<int:post_id>', methods=["POST"])
def edit_user(post_id):
    session['post_id'] = post_id
    if 'user_id' not in session:
        return redirect('/')
    elif Post.validate_post(request.form):
        data = {
            'post_id' : session['post_id'],
            'location' : request.form['location'],
            'date' : request.form['date'],
            'content' : request.form['content'],
            'sasquatches' : request.form['sasquatches']
            }
        Post.editById(data) 
        return redirect('/dashboard')
    return redirect(f"/edit/{session['post_id']}")

# Delete Post
@app.route('/post/delete/<int:post_id>')
def delete_post(post_id):
    if 'user_id' in session:
        Post.deleteById({'post_id' : post_id})
        return redirect('/dashboard')
    return redirect('/')
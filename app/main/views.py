@main.route('/')
def index():
    health = Blog.query.filter_by(category = 'Health').all()
    lifestyle= Blog.query.filter_by(category = 'Lifestyle').all()
    blogs = Blog.query.all()
    technology  = Blog.query.filter_by(category = 'Technology').all() 
    quotes = get_quotes()
    food= Blog.query.filter_by(category = 'Food').all()
    
    return render_template('index.html',blogs =blogs,technology =technology, health = health, lifestyle=  lifestyle, food= food,quotes=quotes)
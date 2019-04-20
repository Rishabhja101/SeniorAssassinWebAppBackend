module.exports = function(app, db) {
    //get all participants
    app.get("/participants", (req, res) => {
        db.collection('participants').find( {} ).toArray((err, item) => {
            if(err){
                res.send({'error': 'an error has occurred'});
            } else {
                res.send(item);
            }
        });
    });

    //get a participant
    app.get('/participants/:name', (req, res) => {
        const name = req.params.name

        db.collection('participants').findOne({name: name}, (err, item) => {
            if (err){
                res.send({ 'error': 'An error has occured' });
            } else{
                res.send(item);
            }
        });
    });

    //delete participant
    app.delete('/participants/delete/:name', (req, res) => {
        const name = req.params.name;

        db.collection('participants').deleteOne({name: name}, (err, item) => {
            if (err){
                res.send({ 'error': 'An error has occured' });
            } else{
                res.send('Person ' + name + ' deleted!');
            }
        });
    });

    //update participant
    app.put('/participants/update', (req, res) => {
        const name = req.body.name;
        const target = req.body.target;
        const person = { 
            name: name,
            target: target
        };

        db.collection('participants').update({name: name}, person, (err, item) => {
            if (err){
                res.send({ 'error': 'An error has occured' });
            } else{
                res.send(item);
            }
        });
    });
    
    // Add Participant
    app.post("/participants/add", (req, res) => {
        const person = {
            name: req.body.name,
            target: ''
        };

        db.collection('participants').insert(person, (err, result) => {
            if(err) {
                res.send({'error': 'An error has occurred'});
            } else {
                res.send(result.ops[0]);
            }
        });
    });
};
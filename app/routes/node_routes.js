const Cryptr = require('cryptr');

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
        const name = req.body.name.toLowerCase();
        let target = req.body.target;
        let kills = 0;
        /*
        if(target != null && target != undefined){
            target = target.toLowerCase();
        }
        */
        
        //let kills = req.body.kills;

        /*
        //if kills or target is null
        if((kills == null || kills == undefined) || (target == null || target == undefined)){
            //set number of kills
            db.collection('participants').findOne({name: name}, (err, item) => {
                if (err){
                    console.log({ 'error': 'An error has occured with fetching scores' });
                } else {
                    //if kills is null
                    if(kills == null || kills == undefined) {
                        kills = item["kills"];
                    }
                    //if target is null
                    if(target == null || target == undefined){
                        target = item["target"];
                    }
                }
            });
        }
        */

        //handle encryption
        db.collection('encryption').find( {} ).toArray((err, item) => {
            if(err){
                console.log({'error': 'an error has occurred with secret key'});
            } else {
                
                const secretKey = item[0]['secretKey'];
                const cryptr = new Cryptr(secretKey);

                target = cryptr.encrypt(target);

                const person = { 
                    name: name,
                    target: target,
                    kills: 0
                };
        
                db.collection('participants').update({name: name}, person, (err, item) => {
                    if (err){
                        res.send({ 'error': 'An error has occured' });
                    } else{
                        res.send(item);
                    }
                });
            }
        });
    });
    
    // Add Participant
    app.post("/participants/add", (req, res) => {
        const person = {
            name: req.body.name.toLowerCase(),
            target: '',
            kills: 0
        };

        db.collection('participants').insert(person, (err, result) => {
            if(err) {
                res.send({'error': 'An error has occurred with post'});
            } else {
                res.send(result.ops[0]);
            }
        });
    });
};
import React from 'react';
import ReactDOM from 'react-dom';



// //
// Main note queue //
// //

class NoteDeleteButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: props.id
        };
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        fetch('http://' + window.location.host + '/notes/delete', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: this.state.id
            })
        });
    }

    render() {
        return (
            <button className="noteHeaderDeleteButton" onClick={this.handleClick}>
                DELETE
            </button>
        );
    }
}

class Note extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            header: props.header,
            body: props.body,
            date: props.date,
            id: props.id,
            qid: props.qid
        };
    }

    render() {
        return(
            <div className="note">
                <div className="noteHeader">
                    <div className="noteHeaderText">
                        <h3>
                            {this.state.header}
                        </h3>
                    </div>
                    <div className="noteHeaderDate">
                        {this.state.date}
                    </div>
                    <div className="noteHeaderDelete">
                        <NoteDeleteButton id={this.state.id}/>
                    </div>
                </div>
                <div className="noteBody">
                    <p>
                        {this.state.body}
                    </p>
                </div>
            </div>
        );
    }
}

class NoteList extends React.Component {
    constructor(props) {
        super(props);
        this.state ={
            qid: props.qid,
            notes: []
        };
    }

    componentWillReceiveProps(nextProps) {
        alert("NoteList receive props");
        this.state = {
            qid: nextProps.qid
        };
        /*fetch('http://' + window.location.host +  "/notes/get" + "?qid=" + this.state.qid)
            .then(result => result.json())
            .then(rcvNotes => this.setState({qid: this.state.qid, notes: rcvNotes}));*/
    }

    render() {
        return(
            <div id="noteList">
                {this.state.notes.map(
                    (note) => <Note
                        header={note.header}
                        body={note.body}
                        date={note.date}
                        id={note.id}
                        qid={note.qid}
                    />
                )}
            </div>
        )
    }
}



// //
// Note add form //
// //

class NoteAddForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            qid: props.qid
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        fetch('http://' + window.location.host + '/notes/add', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                qid: this.state.qid,
                header: this.inputHeader.value,
                body: this.inputBody.value
            })
        });
        event.preventDefault();
    }

    componentWillReceiveProps(nextProps) {
        this.state = {
            qid: nextProps.qid
        };
    }

    render() {
        return (
            <form className="addNote" onSubmit={this.handleSubmit}>
                <label className="addNoteHeader">
                    Title:
                    <input type="text" ref={(input) => this.inputHeader = input} />
                </label>
                <label className="addNoteBody">
                    <input type="text" ref={(input) => this.inputBody = input} />
                </label>
                <input type="submit" value="ADD" />
            </form>
        );
    }
}



// //
// Rendering //
// //

class Page extends React.Component {
    constructor() {
        super();
        this.state = {
            qid: '',
            noteList: <NoteList qid='' />,
            noteAddForm: <NoteAddForm qid='' />
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.state.noteList.setState({qid: this.inputQid.value});
        this.state.noteAddForm.setState({qid: this.inputQid.value});
        this.state.qid = this.inputQid.value;
    }

    render() {
        return (
            <div id="backbone">
                <div id="pageHeader">
                    <form className="searchForm" onSubmit={this.handleSubmit}>
                        <label className="searchFormHeader">
                            <input type="text" ref={(input) => this.inputQid = input} />
                        </label>
                        <input type="submit" value="Get notes!" />
                    </form>
                </div>
                {this.state.noteList}
                {this.state.noteAddForm}
            </div>
        );
    }
}



ReactDOM.render(
    <Page />,
    document.getElementById('backbone-static')
);

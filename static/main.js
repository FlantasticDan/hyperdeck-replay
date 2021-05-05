const aButton = document.getElementById('a')
const bButton = document.getElementById('b')
const cButton = document.getElementById('c')
const dButton = document.getElementById('d')


class DeckControl{
    constructor(button) {
        this.button = button
        this.state = true

        this.button.onclick = () => {this.toggle()}
    }

    toggle() {
        if(this.state)
        {
            this.button.classList.remove('selected')
            this.state = false
        }
        else
        {
            this.button.classList.add('selected')
            this.state = true
        }
    }

    on() {
        this.button.classList.add('selected')
        this.state = true
    }

    off() {
        this.button.classList.remove('selected')
        this.state = false
    }

}

const a = new DeckControl(aButton)
const b = new DeckControl(bButton)
const c = new DeckControl(cButton)
const d = new DeckControl(dButton)

document.getElementById('all').onclick = () => {
    a.on()
    b.on()
    c.on()
    d.on()
}

document.getElementById('none').onclick = () => {
    a.off()
    b.off()
    c.off()
    d.off()
}

const backwardButton = document.getElementById('backward')
const forwardButton = document.getElementById('forward')

class DirectionControl{
    constructor(forward, backward) {
        this.forward = forward
        this.backward = backward
        this.state = 'forward'

        this.forward.onclick = () => {this.toggle()}
        this.backward.onclick = () => {this.toggle()}
    }

    toggle() {
        if(this.state == 'forward')
        {
            this.forward.classList.remove('selected')
            this.backward.classList.add('selected')
            this.state = 'backward'
        }
        else
        {
            this.forward.classList.add('selected')
            this.backward.classList.remove('selected')
            this.state = 'forward'
        }
    }
}

const direction = new DirectionControl(forwardButton, backwardButton)

const socket = io()

function getControlState() {
    return {
        a: a.state,
        b: b.state,
        c: c.state,
        d: d.state
    }
}

class StandardCommandButton{
    constructor(id){
        this.button = document.getElementById(id)
        this.id = id
        this.button.onclick = () => {this.click()}
    }

    click(){
        let payload = {
            decks: getControlState(),
            command: this.id
        }
        socket.emit('standard-command', payload)
    }
}

const live = new StandardCommandButton('live')
const clip = new StandardCommandButton('clip')
const record = new StandardCommandButton('record')
const play = new StandardCommandButton('play')
const stop = new StandardCommandButton('stop')
const previous = new StandardCommandButton('previous')
const next = new StandardCommandButton('next')
const beginning = new StandardCommandButton('beginning')
const end = new StandardCommandButton('end')

class GranularCommandButton{
    constructor(id){
        this.button = document.getElementById(id)
        this.id = id
        this.button.onclick = () => {this.click()}
    }

    click(){
        let payload = {
            decks: getControlState(),
            command: this.id,
            direction: direction.state
        }
        socket.emit('granular-command', payload)
    }
}

const p10 = new GranularCommandButton('10%')
const p25 = new GranularCommandButton('25%')
const p50 = new GranularCommandButton('50%')
const p75 = new GranularCommandButton('75%')
const s10 = new GranularCommandButton('10s')
const s5 = new GranularCommandButton('5s')
const s1 = new GranularCommandButton('1s')
const f1 = new GranularCommandButton('1f')
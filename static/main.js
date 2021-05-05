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

}

const a = new DeckControl(aButton)
const b = new DeckControl(bButton)
const c = new DeckControl(cButton)
const d = new DeckControl(dButton)

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
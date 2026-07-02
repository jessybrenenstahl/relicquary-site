# TouchLink: a virtual touchscreen driver

*Machine-readable Markdown of https://relicquary.com/touchlink.html (content hash 83821c11)*

**TouchLink** is the control-surface lane of **AIM** (RQ MCP LLC's full-stack computer-use operator) and a standalone macOS driver in its own right.

[AIM & the stack](stack.html)

# Touch that lands where you tap.

**TouchLink** is a virtual touchscreen driver for Mac. On its own, it makes touch behave like touch: **your touchscreen works like a touchscreen, and your mouse stays a mouse**. And because it's a virtual driver, it also folds into a larger stack as a programmable control surface, the way AIM uses it.

A working prototype, verified on real hardware. Distribution packaging comes next. macOS 13+.

touchlink verified · real panel

    plug in: your USB touchscreen
    calibrate: tap the four corners · once
    you tap: the button you meant
    it lands: right where you touched ✓
    your mouse: still works as a mouse

01 / THE PROBLEM

## macOS has no good answer for USB touchscreens.

Plug a touchscreen into a Mac and it mostly doesn't behave: your taps land on the wrong screen, in the wrong place, or just move the pointer. macOS treats a touchscreen as a mouse; TouchLink makes it behave like a touchscreen.

### Calibrated to your screen

A quick, guided four-corner tap teaches TouchLink your exact panel and layout, so from then on, your touch lands on the right spot, every time.

4-point matrix

### No kernel hacks

TouchLink runs as a menu-bar app on public macOS frameworks: `IOHIDManager` and a `CGEvent` tap. No kernel extension to break on an OS update.

IOHIDManager · CGEvent

### Right screen, every time

It corrects events for the specific display you've bound the touchscreen to, leaving your other screens untouched. The right surface gets the touch.

display-bound

02 / HOW IT WORKS

## Catch the wrong tap. Post the right one.

TouchLink watches the raw HID stream, recognises the miscalibrated event, applies your calibration, and returns a corrected native event, all on-device.

STAGE 01

#### Monitor

Reads raw USB touchscreen HID reports through `IOHIDManager`.

STAGE 02

#### Match

A `CGEvent` tap catches the miscalibrated pointer event macOS generated.

STAGE 03

#### Correct

Applies your per-device 4-point calibration matrix to the coordinates.

STAGE 04

#### Post

Returns the corrected event to the stream, and the tap lands exactly where you touched.

**On-device, by construction.** Everything happens locally on your Mac through public frameworks. TouchLink needs Input Monitoring and Accessibility permission to read raw HID and post corrected events, and nothing else.

03 / IN THE AIM STACK

## The same primitive, as a control surface.

Inside [AIM](stack.html), TouchLink is the pattern for turning a physical touchscreen into a safe driver of a virtual workspace, under the same bounded-autonomy rules as the rest of the stack.

### ROLE_01 · Observer-first

By default it observes and transforms coordinates: metadata only. No synthetic input is injected and no drivers are mutated without an explicit, approved step.

### ROLE_02 · Focus-preserving

The control-surface lane is designed to route touch into a virtual workspace without stealing focus or duplicating input; the operator's other work keeps running.

### ROLE_03 · Bounded, like the rest

Any real routing or synthetic input sits behind explicit approval: the same "no single part acts unchecked" posture that governs the whole AIM operator.

### ROLE_04 · Cross-machine, research

Extending the lane to route a Windows-owned touchscreen into a Mac workspace is on the roadmap, behind hard safety rails. Not a shipping feature today.

04 / STATUS

## A working prototype, on real hardware.

TouchLink builds, signs, launches, and passes its test suite on one real panel. [HW 2026-06 · verified ↗](record.html#hw-touchlink) Distribution packaging comes next.

Email your panel model and macOS version and we will send current-build instructions, or say “updates” to hear when packaging ships.

hello@relicquary.com · subject “TouchLink”

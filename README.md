# Hooke's Law & Elasticity Simulation

An interactive, high-school-level physics simulation designed to demonstrate the principles of Hooke's Law and the Modulus of Elasticity. This tool provides a **Target-Driven Calculation Model**, allowing students to explore the relationships between force, extension, material properties, and elastic energy by choosing which parameter they want to solve for.

## 🚀 Key Features

### 1. Target-Driven Calculation Model
Unlike traditional simulations where Force is the only independent variable, this tool allows you to select **any** parameter as the calculation target:
- **Force (F)**
- **Extension (ΔL)**
- **Spring Constant (k)**
- **Stress (σ)** (Modulus mode only)
- **Strain (ε)** (Modulus mode only)
- **Young's Modulus (E)** (Modulus mode only)

When a target is selected, its input fields are automatically disabled and highlighted in light blue, indicating that it is now the dependent variable (the "answer") that updates in response to changes in other sliders.

### 2. Dual Simulation Modes
- **Hooke's Law**: Visualize a spring under tension. Focuses on the relationship $F = k \cdot \Delta L$ and Elastic Potential Energy.
- **Modulus of Elasticity**: Visualize a wire/rod. Introduces material-specific properties like Cross-sectional Area ($A$) and Original Length ($L_0$).

### 3. Step-by-Step Solutions
The "Solution" panel provides a real-time, mathematically accurate derivation for the selected target. Formulas are rendered with professional formatting, including fractions and scientific notation, making it an excellent tool for classroom demonstrations.

### 4. Interactive Visuals
- **Dynamic Physics**: The simulation uses damped harmonic oscillation to provide smooth, realistic visual movement of the spring and weights.
- **Magnified View**: For precision, small extensions (especially in wire mode) are shown in a magnified window (up to 20,000x) to make microscopic changes visible.
- **Live Graphing**: Automatically plots either a **Force vs. Extension** or **Stress vs. Strain** curve as you adjust inputs.

## 📚 Physics Implementation

### Formulas
- **Hooke's Law**: $F = k \cdot \Delta L$
- **Elastic Potential Energy**: $U = \frac{1}{2} k (\Delta L)^2$
- **Stress**: $\sigma = \frac{F}{A}$
- **Strain**: $\epsilon = \frac{\Delta L}{L_0}$
- **Young's Modulus**: $E = \frac{\sigma}{\epsilon}$

### Constants
- **Gravity ($g$)**: Fixed at $9.8 \, \text{m/s}^2$ for Mass-to-Force conversions.

## 🛠️ Technical Details

- **Language**: Vanilla HTML5, CSS3, and JavaScript (ES6+).
- **Dependencies**: None. The project is entirely self-contained and works offline.
- **Rendering**: HTML5 Canvas API for the physical simulation and graph.
- **Styling**: Modern CSS with Flexbox for formula rendering and `@keyframes` for UI feedback animations (pulse and fade effects).

## 📖 How to Use

1. **Select Mode**: Use the toggle at the top of the "Simulation Controls" to switch between Hooke's Law and Modulus of Elasticity.
2. **Set Target**: Choose the variable you want to calculate in the "What is being calculated?" section.
3. **Manipulate Inputs**: Use the sliders or numeric input boxes to change the other parameters. Note that the target variable's inputs will be locked.
4. **Analyze**:
    - Watch the **Spring/Wire** deform.
    - Check the **Dashboard** for final values.
    - Read the **Solution** panel to see the mathematical steps taken.
    - Observe the **Graph** to see the linear relationship.

---
*Designed for offline educational use in high school physics labs and classrooms.*

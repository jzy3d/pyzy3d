package org.pyzy3d;
import java.util.HashMap;
import java.util.Map;

import org.jzy3d.bridge.IFrame;
import org.jzy3d.chart.Chart;
import org.jzy3d.chart.factories.AWTChartComponentFactory;
import org.jzy3d.colors.Color;
import org.jzy3d.colors.ColorMapper;
import org.jzy3d.colors.colormaps.ColorMapRainbow;
import org.jzy3d.maths.Coord3ds;
import org.jzy3d.maths.Range;
import org.jzy3d.plot3d.builder.Builder;
import org.jzy3d.plot3d.builder.concrete.OrthonormalGrid;
import org.jzy3d.plot3d.primitives.Scatter;
import org.jzy3d.plot3d.primitives.Shape;
import org.jzy3d.plot3d.rendering.canvas.Quality;

import py4j.GatewayServer;

/**
 * 
 * @see https://www.py4j.org/py4j_java_gateway.html
 * @author Martin Pernollet
 */
public class Pyzy3d {
    protected Quality quality = Quality.Advanced;
    protected Chart chart;
    protected Map<Integer,Chart> charts = new HashMap<Integer,Chart>();

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new Pyzy3d());
        gatewayServer.start();
        System.out.println("Pzy3d Gateway Server Started");
    }

    public Pyzy3d(){
       chart = AWTChartComponentFactory.chart(quality, "newt");
       chart.addMouseCameraController();
    }
    
    /* CHART */

    public Chart getChart() {
        return chart;
    }

    public Chart getOrCreateChart(int id) {
        Chart chart = charts.get(id);
        if(chart==null){
            chart = newChart(Quality.Advanced);
            charts.put(id, chart);
        }
        return chart;
    }
    

    
    public IFrame open(String title, int width, int height){
        return chart.open(title, width, height);
    }
    
    public void clear(){
        chart.clear();
    }
    
    /* PRIMITIVES */
    
    public Scatter scatter(Coord3ds coords){
        Scatter scatter = new Scatter(coords.coordsArray(), coords.colorsArray());
        //scatter.setColor(Color.BLACK);
        chart.getScene().add(scatter);
        return scatter;
    }
    
    public Scatter newScatter(Coord3ds coords){
        Scatter scatter = new Scatter(coords.coordsArray(), coords.colorsArray());
        return scatter;
    }

    /**
     * Initialize a chart. Chart is not registered in Pyzy3d list of managed charts
     * 
     * @param quality
     * @return
     */
    public Chart newChart(Quality quality){
        Chart chart = AWTChartComponentFactory.chart(quality, "newt");
        chart.addMouseCameraController();
        return chart;
    }

    /** Create the object to represent the function over the given range.
     */
    public Shape newSurface(PyFunc3d pyFunction, float xmin, float xmax, float ymin, float ymax, int steps){
        PyMapper mapper = new PyMapper(pyFunction);
        final Shape surface = Builder.buildOrthonormal(new OrthonormalGrid(new Range(xmin, xmax), steps, new Range(ymin, ymax), steps), mapper);
        surface.setColorMapper(new ColorMapper(new ColorMapRainbow(), surface.getBounds().getZmin(), surface.getBounds().getZmax(), new Color(1, 1, 1, .5f)));
        surface.setFaceDisplayed(true);
        surface.setWireframeDisplayed(false);
        return surface;
    }

    
    /**
     * Print coordinates in console for debugging
     * 
     * @param coords
     */
    public void console(Coord3ds coords){
        for (int i = 0; i < coords.x.length; i++) {
            System.out.println(i + "\tx="+ coords.x[i] + "\ty="+ coords.y[i]  + "\tz="+ coords.z[i]  + "\tr="+ coords.r[i]  + "\tg="+ coords.g[i]  + "\tb="+ coords.b[i] + "\ta="+ coords.a[i]);
        }
    }
    
    public static int[][] createFromPy4j(byte[] data) {
        java.nio.ByteBuffer buf = java.nio.ByteBuffer.wrap(data);
        int n = buf.getInt(), m = buf.getInt();
        int[][] matrix = new int[n][m];
        for (int i = 0; i < n; ++i)
           for (int j = 0; j < m; ++j)
              matrix[i][j] = buf.getInt();
        return matrix;//MyClass.create(matrix);
     }

}

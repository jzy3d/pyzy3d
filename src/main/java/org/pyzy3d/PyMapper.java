package org.pyzy3d;

import org.jzy3d.plot3d.builder.Mapper;


public class PyMapper extends Mapper{
    PyFunc3d func3d;
    
    public PyMapper(PyFunc3d func3d) {
        super();
        this.func3d = func3d;
    }

    @Override
    public double f(double x, double y) {
        return func3d.f(x, y);
    }
}

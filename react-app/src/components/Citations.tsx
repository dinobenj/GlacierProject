import { Col, Row, Typography } from "antd";
import React from "react";

const { Paragraph } = Typography;

const Citations: React.FC = () => {
    return (
        <>
            <Row>
                <Col><Paragraph strong style={{
                    color: "white",
                    fontSize: "20px"
                }}>
                    WGMS (2021): Global Glacier Change Bulletin No. 4 (2018-2019).
                    Michael Zemp, Samuel U. Nussbaumer, Isabelle Gärtner-Roer,
                    Jacqueline Bannwart, Frank Paul, and Martin Hoelzle (eds.),
                    ISC (WDS) / IUGG (IACS) / UNEP / UNESCO / WMO, World Glacier
                    Monitoring Service, Zurich, Switzerland, 278 pp.
                    Based on database version
                </Paragraph>
                    <Paragraph style={{
                        color: "blue",
                        fontSize: "20px"
                    }}>
                        <a href="https://doi.org/10.5904/wgms-fog-2021-05">https://doi.org/10.5904/wgms-fog-2021-05.</a>
                    </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col><Paragraph strong style={{
                    color: "white",
                    fontSize: "20px"
                }}>
                    WGMS (2013): Glacier Mass Balance Bulletin No. 12 (2010-2011).
                    Michael Zemp, Samuel U. Nussbaumer, Kathrin Naegeli,
                    Isabelle Gärtner-Roer, Frank Paul, Martin Hoelzle,
                    and Wilfried Haeberli (eds.), ICSU (WDS) / IUGG (IACS) /
                    UNEP / UNESCO / WMO, World Glacier Monitoring Service,
                    Zurich, Switzerland, 106 pp. Based on database version
                </Paragraph>
                    <Paragraph style={{
                        color: "blue",
                        fontSize: "20px"
                    }}>
                        <a href="https://doi.org/10.5904/wgms-fog-2013-11">https://doi.org/10.5904/wgms-fog-2013-11.</a>
                    </Paragraph>
                </Col >
            </Row >
            <Row>
                <Col><Paragraph strong style={{
                    color: "white",
                    fontSize: "20px"
                }}>
                    WGMS (2012): Fluctuations of Glaciers 2005-2010 (Vol. X):
                    Michael Zemp, Holger Frey, Isabelle Gärtner-Roer,
                    Samuel U. Nussbaumer, Martin Hoelzle, Frank Paul,
                    and Wilfried Haeberli (eds.), ICSU (WDS) / IUGG (IACS) /
                    UNEP / UNESCO / WMO, World Glacier Monitoring Service,
                    Zurich, Switzerland. Based on database version
                    <Paragraph style={{
                        color: "blue",
                        fontSize: "20px"
                    }}>
                        <a href="https://doi.org/10.5904/wgms-fog-2012-11">https://doi.org/10.5904/wgms-fog-2012-11.</a>
                    </Paragraph>
                </Paragraph>
                </Col>
            </Row>
            <Row>
                <Col><Paragraph strong style={{
                    color: "white",
                    fontSize: "20px"
                }}>
                    GLIMS and NSIDC (2005, updated 2018): Global Land Ice Measurements
                    from Space glacier database.  Compiled and made available by the
                    international GLIMS community and the National Snow and Ice Data Center,
                    Boulder CO, U.S.A.  DOI:10.7265/N5V98602
                </Paragraph>
                </Col>
            </Row>
        </>
    );
}

export default Citations;



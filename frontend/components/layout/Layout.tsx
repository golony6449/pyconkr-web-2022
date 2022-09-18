import React, { ReactNode } from 'react'
import NavBar from '../core/NavBar'
import NavBarMobile from '../core/NavBarMobile'
import styled from 'styled-components'
import { media } from '../../assets/styles/mixin'

interface LayoutProps {
    locale: string
    pageName: string
    children: ReactNode
}

const Container = styled.div`
    width: 768px;
    margin: 0 auto;
    ${media.mobile(`
        width: 100%;
    `)}
`
const Body = styled.div`
    margin: 3.5rem 0 6rem;
    ${media.mobile(`
        margin: 0;
        padding: 6rem 1.25rem;
    `)}
`

export const Background = styled.div`
    background-color: ${(props) => props.theme.colors.black_10};
    height: 100%;
`

const Layout = (props: LayoutProps) => {
    // TODO: locale을 context로 관리
    return (
        <Background>
            <NavBarMobile locale={props.locale} />
            <NavBar locale={props.locale} />
            <Container>
                <Body>{props.children}</Body>
            </Container>
        </Background>
    )
}

export default Layout

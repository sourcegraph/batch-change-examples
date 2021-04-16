export default function transformer(file, api) {
    const j = api.jscodeshift;
    const root = j(file.source);
    const consoleLogCalls = root.find(j.CallExpression, {
        callee: {
            object: {
                name: 'console'
            },
            property: {
                name: 'warn'
            }
        }
    });
    consoleLogCalls.forEach(p => {
        p.node.callee.property.name = 'log';
    });
    return root.toSource();
};